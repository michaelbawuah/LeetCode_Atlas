"""Validate every shared JSON case, optionally including all C++ runners."""

import json
import os
import re
import subprocess
from pathlib import Path

import pytest

from atlas.runtime import check_result, evaluate, metadata, problem_dirs


def _load_cases():
    entries = []
    for folder in problem_dirs():
        meta = metadata(folder)
        cases = json.loads((folder / "cases.json").read_text())
        if not isinstance(cases, list) or not cases:
            raise ValueError(f"{folder.name}: cases must be a nonempty list")
        names = set()
        for case in cases:
            if not isinstance(case, dict) or not {"name", "expected"} <= case.keys():
                raise ValueError(f"{folder.name}: each case needs name and expected")
            if not isinstance(case["name"], str) or case["name"] in names:
                raise ValueError(f"{folder.name}: fixture names must be unique strings")
            names.add(case["name"])
            if meta["kind"] == "method":
                if not isinstance(case.get("args"), list) or len(case["args"]) != len(
                    meta["args_types"]
                ):
                    raise ValueError(f"{folder.name}/{case['name']}: invalid argument count")
            elif meta["kind"] == "design":
                operations, arguments = case.get("operations"), case.get("arguments")
                expected = case["expected"]
                if (
                    not isinstance(operations, list)
                    or not operations
                    or not isinstance(arguments, list)
                    or not isinstance(expected, list)
                    or len(operations) != len(arguments)
                    or len(operations) != len(expected)
                    or any(not isinstance(args, list) for args in arguments)
                    or operations[0] != meta["class_name"]
                ):
                    raise ValueError(
                        f"{folder.name}/{case['name']}: invalid design fixture lengths or constructor"
                    )
            else:
                raise ValueError(f"{folder.name}: unknown problem kind")
            entries.append((folder, meta, case))
    return entries


CASES = _load_cases()


@pytest.mark.parametrize(
    "folder,meta,case",
    CASES,
    ids=[f"{folder.name}/{case['name']}" for folder, _, case in CASES],
)
def test_python_shared_case(folder, meta, case):
    inputs = {key: case[key] for key in ("args", "operations", "arguments") if key in case}
    actual = evaluate(folder, **inputs)
    assert check_result(meta, actual, case["expected"], args=case.get("args")), (
        f"{folder.name}/{case['name']}: expected {case['expected']!r}, got {actual!r}"
    )


@pytest.mark.skipif(
    not os.environ.get("ATLAS_CPP_BIN_DIR"), reason="C++ runners enabled by ATLAS_CPP_BIN_DIR"
)
def test_cpp_runners_match_all_shared_cases():
    """Batch each executable's JSON-lines input; enforce complete runner coverage."""
    binary_dir = Path(os.environ["ATLAS_CPP_BIN_DIR"]).resolve()
    cpp_folders = [folder for folder in problem_dirs() if (folder / "cpp_runner.cpp").is_file()]
    assert cpp_folders, "No C++ problem runners were discovered"
    suffix = ".exe" if os.name == "nt" else ""
    expected_names = {f"atlas_{folder.name.replace('-', '_')}{suffix}" for folder in cpp_folders}
    assert binary_dir.is_dir(), f"C++ binary directory does not exist: {binary_dir}"
    available_names = {
        path.name
        for path in binary_dir.iterdir()
        if path.is_file() and re.fullmatch(r"atlas_\d{4}_[a-z0-9_]+(?:\.exe)?", path.name)
    }
    assert available_names == expected_names, (
        f"C++ runner coverage mismatch: missing={sorted(expected_names - available_names)}, "
        f"unexpected={sorted(available_names - expected_names)}"
    )
    for folder in cpp_folders:
        binary = binary_dir / f"atlas_{folder.name.replace('-', '_')}{suffix}"
        assert os.access(binary, os.X_OK), f"Runner is not executable: {binary}"
        entries = [(meta, case) for current, meta, case in CASES if current == folder]
        assert all(meta["kind"] == "method" for meta, _ in entries), (
            "C++ batch adapter expects method cases"
        )
        payload = "".join(json.dumps(case["args"]) + "\n" for _, case in entries)
        result = subprocess.run(
            [str(binary)], input=payload, text=True, capture_output=True, timeout=30, check=False
        )
        assert result.returncode == 0, (
            f"{folder.name} runner exited {result.returncode}: {result.stderr}"
        )
        lines = result.stdout.splitlines()
        assert len(lines) == len(entries), (
            f"{folder.name}: expected {len(entries)} JSON result lines, received {len(lines)}"
        )
        for line, (meta, case) in zip(lines, entries, strict=True):
            try:
                actual = json.loads(line)
            except json.JSONDecodeError as error:
                pytest.fail(f"{folder.name}/{case['name']}: invalid runner JSON: {error}")
            assert check_result(meta, actual, case["expected"], args=case.get("args")), (
                f"{folder.name}/{case['name']}: C++ expected {case['expected']!r}, got {actual!r}"
            )
            python_result = evaluate(folder, args=case["args"])
            assert check_result(meta, actual, python_result, args=case.get("args")), (
                f"{folder.name}/{case['name']}: C++/Python disagreement"
            )

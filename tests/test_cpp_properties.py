"""Reproducible generated parity checks across the Python and C++ tracks."""

import json
import os
import random
import subprocess
from pathlib import Path

import pytest

from atlas.runtime import check_result, evaluate, metadata, problem_dirs

FOLDERS = [
    "0001-two-sum",
    "0049-group-anagrams",
    "0238-product-of-array-except-self",
    "0015-3sum",
    "0003-longest-substring-without-repeating-characters",
    "0020-valid-parentheses",
    "0739-daily-temperatures",
    "0033-search-in-rotated-sorted-array",
    "0206-reverse-linked-list",
    "0198-house-robber",
]


def test_every_cpp_counterpart_has_a_generated_case_strategy():
    discovered = {folder.name for folder in problem_dirs() if (folder / "solution.cpp").is_file()}
    assert set(FOLDERS) == discovered, "Add a parity generator when adding a C++ counterpart"


def generated_args(folder, rng):
    if folder == "0001-two-sum":
        nums = rng.sample(range(-100, 101), rng.randint(2, 15))
        a, b = rng.sample(range(len(nums)), 2)
        return [nums, nums[a] + nums[b]]
    if folder == "0049-group-anagrams":
        words = [
            "".join(rng.choices("abcd", k=rng.randint(0, 8))) for _ in range(rng.randint(1, 20))
        ]
        return [words]
    if folder == "0238-product-of-array-except-self":
        return [[rng.randint(-3, 3) for _ in range(rng.randint(2, 10))]]
    if folder == "0015-3sum":
        return [[rng.randint(-20, 20) for _ in range(rng.randint(3, 15))]]
    if folder == "0003-longest-substring-without-repeating-characters":
        return ["".join(rng.choices("abCD019! ", k=rng.randint(0, 50)))]
    if folder == "0020-valid-parentheses":
        return ["".join(rng.choices("()[]{}", k=rng.randint(1, 30)))]
    if folder == "0739-daily-temperatures":
        return [[rng.randint(30, 100) for _ in range(rng.randint(1, 40))]]
    if folder == "0033-search-in-rotated-sorted-array":
        values = sorted(rng.sample(range(-100, 101), rng.randint(1, 40)))
        pivot = rng.randrange(len(values))
        values = values[pivot:] + values[:pivot]
        target = rng.choice(values) if rng.choice([True, False]) else 500
        return [values, target]
    if folder == "0206-reverse-linked-list":
        return [[rng.randint(-100, 100) for _ in range(rng.randint(0, 40))]]
    if folder == "0198-house-robber":
        return [[rng.randint(0, 20) for _ in range(rng.randint(1, 15))]]
    raise ValueError(f"No generator for {folder}")


@pytest.mark.skipif(
    not os.environ.get("ATLAS_CPP_BIN_DIR"), reason="C++ runners enabled by ATLAS_CPP_BIN_DIR"
)
@pytest.mark.parametrize("folder", FOLDERS)
def test_generated_cpp_python_parity(folder):
    """150 cases per problem; Python has independently checked property oracles."""
    rng = random.Random(20261012 + int(folder.split("-", 1)[0]))
    cases = [generated_args(folder, rng) for _ in range(150)]
    binary_dir = Path(os.environ["ATLAS_CPP_BIN_DIR"]).resolve()
    suffix = ".exe" if os.name == "nt" else ""
    binary = binary_dir / f"atlas_{folder.replace('-', '_')}{suffix}"
    result = subprocess.run(
        [str(binary)],
        input="".join(json.dumps(args) + "\n" for args in cases),
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    lines = result.stdout.splitlines()
    assert len(lines) == len(cases), f"{folder}: missing or extra result lines"
    meta = metadata(folder)
    for index, (line, args) in enumerate(zip(lines, cases, strict=True)):
        actual = json.loads(line)
        expected = evaluate(folder, args=args)
        if folder == "0001-two-sum":
            # Multiple pairs can be valid; compare the specification rather than pair choice.
            assert isinstance(actual, list) and len(actual) == 2
            assert all(type(i) is int and 0 <= i < len(args[0]) for i in actual)
            assert actual[0] != actual[1]
            assert args[0][actual[0]] + args[0][actual[1]] == args[1]
        else:
            assert check_result(meta, actual, expected), (folder, index, args, actual, expected)

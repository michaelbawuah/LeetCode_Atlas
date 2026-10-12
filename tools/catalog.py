"""Generate the browsable index from actual implementations and metadata."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def collect(root: Path = ROOT) -> list[dict]:
    entries = []
    ids = set()
    for folder in sorted((root / "problems").iterdir()):
        if not folder.is_dir() or not (folder / "meta.json").exists():
            continue
        meta = json.loads((folder / "meta.json").read_text())
        expected = f"{meta['id']:04d}-{meta['slug']}"
        if folder.name != expected:
            raise ValueError(f"Folder {folder.name} does not match canonical ID/slug {expected}")
        if meta["id"] in ids:
            raise ValueError(f"Duplicate problem ID {meta['id']}")
        ids.add(meta["id"])
        if meta["difficulty"] not in {"Easy", "Medium", "Hard"}:
            raise ValueError(f"Invalid difficulty: {folder.name}")
        if not meta["patterns"] or any(
            not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", p) for p in meta["patterns"]
        ):
            raise ValueError(f"Use kebab-case pattern tags: {folder.name}")
        if meta["kind"] not in {"method", "design"}:
            raise ValueError(f"Unknown invocation kind: {folder.name}")
        if meta["checker"] not in {
            "exact",
            "unordered",
            "unordered_groups",
            "unordered_rows",
            "topological_order",
            "approx",
            "longest_palindrome",
            "gas_station",
            "graph_adjacency",
        }:
            raise ValueError(f"Unknown checker: {folder.name}")
        if not isinstance(meta["args_types"], list) or any(
            t not in {"value", "listnode", "listnode_cycle", "treenode", "graphnode"}
            for t in meta["args_types"]
        ):
            raise ValueError(f"Unknown argument adapter: {folder.name}")
        if meta["return_type"] not in {"value", "listnode", "treenode", "graphnode"}:
            raise ValueError(f"Unknown result adapter: {folder.name}")
        if meta["kind"] == "method":
            if not isinstance(meta.get("method"), str) or not meta["method"].isidentifier():
                raise ValueError(f"Method declaration requires a method name: {folder.name}")
        elif (
            not isinstance(meta.get("class_name"), str)
            or not meta["class_name"].isidentifier()
            or meta["args_types"]
            or meta["return_type"] != "value"
        ):
            raise ValueError(f"Design declaration requires a class and value result: {folder.name}")
        checker_declarations = {
            "longest_palindrome": (["value"], "value"),
            "gas_station": (["value", "value"], "value"),
            "graph_adjacency": (["graphnode"], "graphnode"),
        }
        if meta["checker"] in checker_declarations:
            adapters, result_adapter = checker_declarations[meta["checker"]]
            if (
                meta["kind"] != "method"
                or meta["args_types"] != adapters
                or meta["return_type"] != result_adapter
            ):
                raise ValueError(f"Checker declaration does not match its adapters: {folder.name}")
        if meta["checker"] == "approx" and (
            meta["kind"] != "method" or meta["return_type"] != "value"
        ):
            raise ValueError(f"Approximate checker requires a numeric value result: {folder.name}")
        if "result_from_arg" in meta:
            index = meta["result_from_arg"]
            if (
                meta["kind"] != "method"
                or type(index) is not int
                or not 0 <= index < len(meta["args_types"])
                or meta["args_types"][index] != meta["return_type"]
            ):
                raise ValueError(f"Invalid in-place result argument: {folder.name}")
        if meta["judge_status"] not in {"not_recorded", "accepted"}:
            raise ValueError(f"Unknown judge status: {folder.name}")
        if meta["judge_status"] == "accepted" and not meta.get("submission_evidence"):
            raise ValueError(f"Accepted status requires dated submission evidence: {folder.name}")
        for filename in ("solution.py", "README.md", "cases.json", "test_properties.py"):
            if not (folder / filename).is_file():
                raise ValueError(f"Missing {filename}: {folder.name}")
        if (folder / "solution.cpp").exists() != (folder / "cpp_runner.cpp").exists():
            raise ValueError(f"C++ implementation and runner must both exist: {folder.name}")
        cases = json.loads((folder / "cases.json").read_text())
        if not cases or len({c["name"] for c in cases}) != len(cases):
            raise ValueError(f"Empty or duplicated named fixtures: {folder.name}")
        for case in cases:
            if "expected" not in case:
                raise ValueError(f"Fixture needs expected result: {folder.name}")
            if meta["checker"] == "approx" and (
                type(case["expected"]) not in {int, float} or not math.isfinite(case["expected"])
            ):
                raise ValueError(
                    f"Approximate fixture requires a finite numeric result: {folder.name}"
                )
            if meta["checker"] == "longest_palindrome" and not (
                isinstance(case["expected"], str)
                or (type(case["expected"]) is int and case["expected"] >= 0)
            ):
                raise ValueError(
                    f"Palindrome fixture requires a reference string or length: {folder.name}"
                )
            if meta["checker"] == "gas_station" and type(case["expected"]) is not int:
                raise ValueError(
                    f"Gas-station fixture requires an integer start or -1: {folder.name}"
                )
            if meta["kind"] == "method":
                if (
                    not isinstance(case.get("args"), list)
                    or len(case["args"]) != len(meta["args_types"])
                    or "operations" in case
                    or "arguments" in case
                ):
                    raise ValueError(f"Fixture arity mismatch: {folder.name}/{case['name']}")
            else:
                if (
                    not isinstance(case.get("operations"), list)
                    or not case["operations"]
                    or not isinstance(case.get("arguments"), list)
                    or not isinstance(case["expected"], list)
                    or not (
                        len(case["operations"]) == len(case["arguments"]) == len(case["expected"])
                    )
                    or case["operations"][0] != meta["class_name"]
                    or any(not isinstance(values, list) for values in case["arguments"])
                    or "args" in case
                ):
                    raise ValueError(f"Design fixture arity mismatch: {folder.name}/{case['name']}")
        entry = dict(meta)
        entry.update(
            folder=folder.name,
            languages=["Python"] + (["C++23"] if (folder / "solution.cpp").exists() else []),
            fixed_cases=len(cases),
            url=f"https://leetcode.com/problems/{meta['slug']}/",
        )
        entries.append(entry)
    return sorted(entries, key=lambda e: e["id"])


def render(entries: list[dict]) -> dict[str, str]:
    counts = Counter(language for e in entries for language in e["languages"])
    accepted = sum(e["judge_status"] == "accepted" for e in entries)
    catalog = {
        "schema_version": 1,
        "distinct_problems": len(entries),
        "implementations": dict(counts),
        "fixed_cases": sum(e["fixed_cases"] for e in entries),
        "official_acceptances_recorded": accepted,
        "targets": {"distinct_problems": 300, "Python": 300, "C++23": 150},
        "problems": entries,
    }
    lines = [
        "# Problem index",
        "",
        "Generated by `python tools/catalog.py`. Counts represent distinct problem IDs;",
        "additional languages do not increase the problem count.",
        "",
        f"**{len(entries)} problems · {counts['Python']} Python · {counts['C++23']} C++23**",
        "",
        "[Pattern index](pattern-index.md) · [Practice route](roadmap.md) · [Verification](verification.md)",
        "",
        "| ID | Problem | Difficulty | Pattern | Implementations | Explanation | Fixtures |",
        "| ---: | --- | --- | --- | --- | --- | ---: |",
    ]
    for e in entries:
        path = f"../problems/{e['folder']}"
        impl = f"[Python]({path}/solution.py)"
        if "C++23" in e["languages"]:
            impl += f" · [C++23]({path}/solution.cpp)"
        patterns = ", ".join(e["patterns"])
        lines.append(
            f"| {e['id']} | [{e['title']}]({e['url']}) | {e['difficulty']} | {patterns} | "
            f"{impl} | [Notes]({path}/README.md) | [{e['fixed_cases']}]({path}/cases.json) |"
        )
    lines.extend(
        [
            "",
            f"Official LeetCode acceptances recorded: **{accepted}**. Local verification and",
            "official judge results are tracked separately; see each problem's metadata.",
            "",
        ]
    )
    groups = defaultdict(list)
    for e in entries:
        for pattern in e["patterns"]:
            groups[pattern].append(e)
    pattern_lines = [
        "# Pattern index",
        "",
        "Generated from problem metadata. One problem can illustrate several patterns.",
        "",
        "[How to choose a pattern](patterns.md) · [All problems](problems.md)",
        "",
    ]
    for pattern, group in sorted(groups.items()):
        pattern_lines.extend([f"## {pattern}", ""])
        pattern_lines.extend(
            f"- [{e['id']}. {e['title']}](../problems/{e['folder']}/README.md) — {e['difficulty']}"
            for e in group
        )
        pattern_lines.append("")
    readme = (ROOT / "README.md").read_text()
    stats_pattern = r"<!-- atlas:stats:start -->.*?<!-- atlas:stats:end -->"
    if len(re.findall(stats_pattern, readme, flags=re.DOTALL)) != 1:
        raise ValueError("README needs exactly one generated atlas statistics section")
    stats = (
        "<!-- atlas:stats:start -->\n"
        f"**{len(entries)} distinct problems · {counts['Python']} Python solutions · "
        f"{counts['C++23']} C++23 counterparts**\n"
        "<!-- atlas:stats:end -->"
    )
    readme = re.sub(stats_pattern, lambda match: stats, readme, flags=re.DOTALL)
    return {
        "README.md": readme,
        "catalog.json": json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        "docs/problems.md": "\n".join(lines),
        "docs/pattern-index.md": "\n".join(pattern_lines) + "\n",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated files are stale")
    args = parser.parse_args()
    errors = []
    for relative, content in render(collect()).items():
        target = ROOT / relative
        if args.check:
            if not target.exists() or target.read_text() != content:
                errors.append(relative)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
    if errors:
        print("Stale generated files: " + ", ".join(errors), file=sys.stderr)
        return 1
    print("Catalog checked." if args.check else "Catalog generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

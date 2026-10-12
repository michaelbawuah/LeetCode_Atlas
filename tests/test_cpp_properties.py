"""Reproducible generated parity checks across the Python and C++ tracks."""

import json
import os
import random
import subprocess
from collections import Counter, deque
from pathlib import Path

import pytest

from atlas.runtime import TreeNode, check_result, evaluate, metadata, problem_dirs, tree_to_json

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
    "0128-longest-consecutive-sequence",
    "0053-maximum-subarray",
    "0056-merge-intervals",
    "0057-insert-interval",
    "0076-minimum-window-substring",
    "0150-evaluate-reverse-polish-notation",
    "0875-koko-eating-bananas",
    "0215-kth-largest-element-in-an-array",
    "0019-remove-nth-node-from-end-of-list",
    "0098-validate-binary-search-tree",
    "0207-course-schedule",
    "0684-redundant-connection",
    "0994-rotting-oranges",
    "0322-coin-change",
    "0300-longest-increasing-subsequence",
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
    if folder == "0128-longest-consecutive-sequence":
        return [[rng.randint(-20, 20) for _ in range(rng.randint(0, 40))]]
    if folder == "0053-maximum-subarray":
        return [[rng.randint(-20, 20) for _ in range(rng.randint(1, 30))]]
    if folder == "0056-merge-intervals":
        return [[sorted(rng.sample(range(50), 2)) for _ in range(rng.randint(1, 15))]]
    if folder == "0057-insert-interval":
        intervals = []
        cursor = 0
        for _ in range(rng.randint(0, 12)):
            start = cursor + rng.randint(0, 3)
            end = start + rng.randint(0, 5)
            intervals.append([start, end])
            cursor = end + rng.randint(1, 4)
        return [intervals, sorted(rng.sample(range(cursor + 10), 2))]
    if folder == "0076-minimum-window-substring":
        s = "".join(rng.choices("aAbBc", k=rng.randint(1, 35)))
        t = "".join(rng.choices("aAbBc", k=rng.randint(1, 6)))
        return [s, t]
    if folder == "0150-evaluate-reverse-polish-notation":
        a, b, c = (rng.randint(-50, 50) for _ in range(3))
        first, second = rng.choices(["+", "-", "*", "/"], k=2)
        if first == "/" and b == 0:
            b = 1
        if second == "/" and c == 0:
            c = 1
        return [[str(a), str(b), first, str(c), second]]
    if folder == "0875-koko-eating-bananas":
        piles = [rng.randint(1, 1000) for _ in range(rng.randint(1, 12))]
        return [piles, rng.randint(len(piles), 20 * len(piles))]
    if folder == "0215-kth-largest-element-in-an-array":
        nums = [rng.randint(-100, 100) for _ in range(rng.randint(1, 40))]
        return [nums, rng.randint(1, len(nums))]
    if folder == "0019-remove-nth-node-from-end-of-list":
        nums = [rng.randint(0, 100) for _ in range(rng.randint(1, 30))]
        return [nums, rng.randint(1, len(nums))]
    if folder == "0098-validate-binary-search-tree":
        root = TreeNode(rng.randint(-20, 20))
        pending = deque([(root, 0)])
        while pending:
            node, depth = pending.popleft()
            if depth == 4:
                continue
            for side in ("left", "right"):
                if rng.random() < 0.65:
                    child = TreeNode(rng.randint(-20, 20))
                    setattr(node, side, child)
                    pending.append((child, depth + 1))
        return [tree_to_json(root)]
    if folder == "0207-course-schedule":
        count = rng.randint(1, 10)
        possibilities = [[a, b] for a in range(count) for b in range(count)]
        return [count, rng.sample(possibilities, rng.randint(0, min(len(possibilities), 16)))]
    if folder == "0684-redundant-connection":
        count = rng.randint(3, 10)
        edges = [sorted([node, rng.randrange(1, node)]) for node in range(2, count + 1)]
        present = {tuple(sorted(edge)) for edge in edges}
        choices = [
            [a, b]
            for a in range(1, count + 1)
            for b in range(a + 1, count + 1)
            if (a, b) not in present
        ]
        edges.append(rng.choice(choices))
        rng.shuffle(edges)
        return [edges]
    if folder == "0994-rotting-oranges":
        rows, columns = rng.randint(1, 5), rng.randint(1, 5)
        return [[[rng.randint(0, 2) for _ in range(columns)] for _ in range(rows)]]
    if folder == "0322-coin-change":
        return [rng.sample(range(1, 21), rng.randint(1, 6)), rng.randint(0, 80)]
    if folder == "0300-longest-increasing-subsequence":
        return [[rng.randint(-100, 100) for _ in range(rng.randint(1, 30))]]
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
        elif folder == "0076-minimum-window-substring":
            # Generated inputs can have tied shortest windows, beyond the unique-answer contract.
            assert isinstance(actual, str) and len(actual) == len(expected)
            if actual:
                assert actual in args[0]
                counts = Counter(actual)
                assert all(counts[letter] >= needed for letter, needed in Counter(args[1]).items())
        else:
            assert check_result(meta, actual, expected, args=args), (
                folder,
                index,
                args,
                actual,
                expected,
            )

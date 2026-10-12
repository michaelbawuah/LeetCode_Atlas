"""Reproducible generated parity checks across the Python and C++ tracks."""

import importlib.util
import inspect
import json
import os
import random
import subprocess
from collections import Counter, deque
from copy import deepcopy
from functools import lru_cache
from pathlib import Path
from uuid import uuid4

import pytest

from atlas.runtime import TreeNode, check_result, evaluate, metadata, problem_dirs, tree_to_json

LEGACY_FOLDERS = [
    "0001-two-sum",
    "0003-longest-substring-without-repeating-characters",
    "0011-container-with-most-water",
    "0015-3sum",
    "0019-remove-nth-node-from-end-of-list",
    "0020-valid-parentheses",
    "0021-merge-two-sorted-lists",
    "0022-generate-parentheses",
    "0024-swap-nodes-in-pairs",
    "0033-search-in-rotated-sorted-array",
    "0039-combination-sum",
    "0042-trapping-rain-water",
    "0046-permutations",
    "0049-group-anagrams",
    "0053-maximum-subarray",
    "0055-jump-game",
    "0056-merge-intervals",
    "0057-insert-interval",
    "0062-unique-paths",
    "0070-climbing-stairs",
    "0071-simplify-path",
    "0072-edit-distance",
    "0074-search-a-2d-matrix",
    "0076-minimum-window-substring",
    "0078-subsets",
    "0094-binary-tree-inorder-traversal",
    "0098-validate-binary-search-tree",
    "0100-same-tree",
    "0104-maximum-depth-of-binary-tree",
    "0105-construct-binary-tree-from-preorder-and-inorder-traversal",
    "0112-path-sum",
    "0121-best-time-to-buy-and-sell-stock",
    "0128-longest-consecutive-sequence",
    "0134-gas-station",
    "0139-word-break",
    "0146-lru-cache",
    "0150-evaluate-reverse-polish-notation",
    "0152-maximum-product-subarray",
    "0155-min-stack",
    "0169-majority-element",
    "0198-house-robber",
    "0199-binary-tree-right-side-view",
    "0201-bitwise-and-of-numbers-range",
    "0206-reverse-linked-list",
    "0207-course-schedule",
    "0208-implement-trie-prefix-tree",
    "0213-house-robber-ii",
    "0215-kth-largest-element-in-an-array",
    "0217-contains-duplicate",
    "0230-kth-smallest-element-in-a-bst",
    "0238-product-of-array-except-self",
    "0239-sliding-window-maximum",
    "0242-valid-anagram",
    "0300-longest-increasing-subsequence",
    "0307-range-sum-query-mutable",
    "0322-coin-change",
    "0338-counting-bits",
    "0347-top-k-frequent-elements",
    "0416-partition-equal-subset-sum",
    "0509-fibonacci-number",
    "0518-coin-change-ii",
    "0543-diameter-of-binary-tree",
    "0547-number-of-provinces",
    "0560-subarray-sum-equals-k",
    "0684-redundant-connection",
    "0695-max-area-of-island",
    "0703-kth-largest-element-in-a-stream",
    "0704-binary-search",
    "0739-daily-temperatures",
    "0743-network-delay-time",
    "0746-min-cost-climbing-stairs",
    "0875-koko-eating-bananas",
    "0981-time-based-key-value-store",
    "0994-rotting-oranges",
    "1584-min-cost-to-connect-all-points",
]

NEW_FOLDERS = [
    "0002-add-two-numbers",
    "0007-reverse-integer",
    "0009-palindrome-number",
    "0012-integer-to-roman",
    "0013-roman-to-integer",
    "0023-merge-k-sorted-lists",
    "0028-find-the-index-of-the-first-occurrence-in-a-string",
    "0031-next-permutation",
    "0032-longest-valid-parentheses",
    "0058-length-of-last-word",
    "0061-rotate-list",
    "0063-unique-paths-ii",
    "0064-minimum-path-sum",
    "0067-add-binary",
    "0075-sort-colors",
    "0082-remove-duplicates-from-sorted-list-ii",
    "0083-remove-duplicates-from-sorted-list",
    "0086-partition-list",
    "0088-merge-sorted-array",
    "0096-unique-binary-search-trees",
    "0101-symmetric-tree",
    "0103-binary-tree-zigzag-level-order-traversal",
    "0107-binary-tree-level-order-traversal-ii",
    "0118-pascals-triangle",
    "0119-pascals-triangle-ii",
    "0120-triangle",
    "0122-best-time-to-buy-and-sell-stock-ii",
    "0137-single-number-ii",
    "0151-reverse-words-in-a-string",
    "0171-excel-sheet-column-number",
    "0205-isomorphic-strings",
    "0221-maximal-square",
    "0222-count-complete-tree-nodes",
    "0240-search-a-2d-matrix-ii",
    "0279-perfect-squares",
    "0287-find-the-duplicate-number",
    "0310-minimum-height-trees",
    "0344-reverse-string",
    "0349-intersection-of-two-arrays",
    "0404-sum-of-left-leaves",
    "0433-minimum-genetic-mutation",
    "0454-4sum-ii",
    "0496-next-greater-element-i",
    "0513-find-bottom-left-tree-value",
    "0515-find-largest-value-in-each-tree-row",
    "0516-longest-palindromic-subsequence",
    "0525-contiguous-array",
    "0542-01-matrix",
    "0583-delete-operation-for-two-strings",
    "0622-design-circular-queue",
    "0658-find-k-closest-elements",
    "0712-minimum-ascii-delete-sum-for-two-strings",
    "0714-best-time-to-buy-and-sell-stock-with-transaction-fee",
    "0740-delete-and-earn",
    "0752-open-the-lock",
    "0797-all-paths-from-source-to-target",
    "0802-find-eventual-safe-states",
    "0841-keys-and-rooms",
    "0886-possible-bipartition",
    "0901-online-stock-span",
    "0909-snakes-and-ladders",
    "0931-minimum-falling-path-sum",
    "0933-number-of-recent-calls",
    "0938-range-sum-of-bst",
    "0947-most-stones-removed-with-same-row-or-column",
    "1011-capacity-to-ship-packages-within-d-days",
    "1020-number-of-enclaves",
    "1094-car-pooling",
    "1137-n-th-tribonacci-number",
    "1220-count-vowels-permutation",
    "1319-number-of-operations-to-make-network-connected",
    "1448-count-good-nodes-in-binary-tree",
    "1631-path-with-minimum-effort",
    "1926-nearest-exit-from-entrance-in-maze",
    "1971-find-if-path-exists-in-graph",
]

ADDED_FOLDERS = [
    "0004-median-of-two-sorted-arrays",
    "0005-longest-palindromic-substring",
    "0006-zigzag-conversion",
    "0008-string-to-integer-atoi",
    "0010-regular-expression-matching",
    "0016-3sum-closest",
    "0017-letter-combinations-of-a-phone-number",
    "0018-4sum",
    "0025-reverse-nodes-in-k-group",
    "0036-valid-sudoku",
    "0038-count-and-say",
    "0040-combination-sum-ii",
    "0044-wildcard-matching",
    "0047-permutations-ii",
    "0048-rotate-image",
    "0050-powx-n",
    "0054-spiral-matrix",
    "0073-set-matrix-zeroes",
    "0090-subsets-ii",
    "0091-decode-ways",
    "0092-reverse-linked-list-ii",
    "0097-interleaving-string",
    "0102-binary-tree-level-order-traversal",
    "0108-convert-sorted-array-to-binary-search-tree",
    "0110-balanced-binary-tree",
    "0113-path-sum-ii",
    "0114-flatten-binary-tree-to-linked-list",
    "0115-distinct-subsequences",
    "0123-best-time-to-buy-and-sell-stock-iii",
    "0124-binary-tree-maximum-path-sum",
    "0127-word-ladder",
    "0129-sum-root-to-leaf-numbers",
    "0130-surrounded-regions",
    "0131-palindrome-partitioning",
    "0132-palindrome-partitioning-ii",
    "0141-linked-list-cycle",
    "0143-reorder-list",
    "0153-find-minimum-in-rotated-sorted-array",
    "0162-find-peak-element",
    "0167-two-sum-ii-input-array-is-sorted",
    "0188-best-time-to-buy-and-sell-stock-iv",
    "0189-rotate-array",
    "0200-number-of-islands",
    "0209-minimum-size-subarray-sum",
    "0210-course-schedule-ii",
    "0211-design-add-and-search-words-data-structure",
    "0225-implement-stack-using-queues",
    "0232-implement-queue-using-stacks",
    "0234-palindrome-linked-list",
    "0235-lowest-common-ancestor-of-a-binary-search-tree",
    "0236-lowest-common-ancestor-of-a-binary-tree",
    "0295-find-median-from-data-stream",
    "0304-range-sum-query-2d-immutable",
    "0312-burst-balloons",
    "0329-longest-increasing-path-in-a-matrix",
    "0337-house-robber-iii",
    "0377-combination-sum-iv",
    "0399-evaluate-division",
    "0417-pacific-atlantic-water-flow",
    "0424-longest-repeating-character-replacement",
    "0494-target-sum",
    "0567-permutation-in-string",
    "0641-design-circular-deque",
    "0673-number-of-longest-increasing-subsequence",
    "0729-my-calendar-i",
    "0785-is-graph-bipartite",
    "0787-cheapest-flights-within-k-stops",
    "0881-boats-to-save-people",
    "0934-shortest-bridge",
    "1143-longest-common-subsequence",
    "1162-as-far-from-land-as-possible",
    "1192-critical-connections-in-a-network",
    "1254-number-of-closed-islands",
    "1462-course-schedule-iv",
    "2050-parallel-courses-iii",
]

PER_PROBLEM_FOLDERS = NEW_FOLDERS + ADDED_FOLDERS
FOLDERS = sorted(LEGACY_FOLDERS + PER_PROBLEM_FOLDERS)


def validate_counterpart_coverage(discovered):
    registered = set(FOLDERS)
    if len(FOLDERS) != 225 or len(registered) != 225 or discovered != registered:
        raise ValueError(
            f"C++ strategy coverage mismatch: missing={sorted(registered - discovered)}, "
            f"unexpected={sorted(discovered - registered)}"
        )


@lru_cache(maxsize=None)
def load_parity_generator(path):
    path = Path(path).resolve()
    if not path.is_file():
        raise ValueError(f"Missing per-problem parity module: {path}")
    spec = importlib.util.spec_from_file_location(f"atlas_parity_{uuid4().hex}", path)
    if spec is None or spec.loader is None:
        raise ValueError(f"Cannot load parity module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    generator = getattr(module, "generate", None)
    if not callable(generator):
        raise ValueError(f"Parity module must define callable generate(rng): {path}")
    parameters = list(inspect.signature(generator).parameters.values())
    if len(parameters) != 1 or parameters[0].kind not in {
        inspect.Parameter.POSITIONAL_ONLY,
        inspect.Parameter.POSITIONAL_OR_KEYWORD,
    }:
        raise ValueError(f"Parity generator must accept exactly one RNG parameter: {path}")
    return generator


def validate_generated_payload(meta, payload):
    if not isinstance(payload, list):
        raise ValueError("Generated payload must be a JSON argument array")

    def json_value(value):
        if value is None or type(value) in {str, bool, int, float}:
            return True
        if isinstance(value, list):
            return all(json_value(item) for item in value)
        if isinstance(value, dict):
            return all(type(key) is str and json_value(item) for key, item in value.items())
        return False

    if not json_value(payload):
        raise ValueError("Generated payload must contain native JSON values")
    try:
        json.dumps(payload, allow_nan=False)
    except (TypeError, ValueError) as error:
        raise ValueError("Generated payload must contain finite JSON values") from error
    if meta["kind"] == "method":
        if len(payload) != len(meta["args_types"]):
            raise ValueError("Generated method payload does not match metadata arity")
    elif meta["kind"] == "design":
        if len(payload) != 2:
            raise ValueError("Generated design payload requires operations and arguments")
        operations, arguments = payload
        if (
            not isinstance(operations, list)
            or not operations
            or not isinstance(arguments, list)
            or len(operations) != len(arguments)
            or any(not isinstance(operation, str) for operation in operations)
            or any(not isinstance(values, list) for values in arguments)
            or operations[0] != meta["class_name"]
            or any(
                operation.startswith("_") or operation == meta["class_name"]
                for operation in operations[1:]
            )
        ):
            raise ValueError("Generated design payload has invalid operation shape or constructor")
    else:
        raise ValueError("Generated payload uses an unknown invocation kind")
    return deepcopy(payload)


def test_every_cpp_counterpart_has_a_generated_case_strategy():
    discovered = {folder.name for folder in problem_dirs() if (folder / "solution.cpp").is_file()}
    validate_counterpart_coverage(discovered)
    root = Path(__file__).resolve().parents[1]
    for folder in PER_PROBLEM_FOLDERS:
        generator = load_parity_generator(root / "problems" / folder / "parity.py")
        meta = metadata(folder)
        seed = 20261012 + int(folder.split("-", 1)[0])
        first_rng, second_rng = random.Random(seed), random.Random(seed)
        first = [validate_generated_payload(meta, generator(first_rng)) for _ in range(3)]
        second = [validate_generated_payload(meta, generator(second_rng)) for _ in range(3)]
        assert first == second, f"{folder}: use the supplied RNG for reproducible parity inputs"


def _random_tree(rng, *, nonempty=False, unique=False):
    if not nonempty and rng.random() < 0.15:
        return None
    root = TreeNode(rng.randint(-100, 100))
    pending = deque([(root, 0)])
    nodes = []
    while pending:
        node, depth = pending.popleft()
        nodes.append(node)
        if depth == 4:
            continue
        for side in ("left", "right"):
            if rng.random() < 0.65:
                child = TreeNode(rng.randint(-100, 100))
                setattr(node, side, child)
                pending.append((child, depth + 1))
    if unique:
        for node, value in zip(nodes, rng.sample(range(-1000, 1001), len(nodes)), strict=True):
            node.val = value
    return root


def _tree_traversals(root):
    preorder, inorder = [], []

    def visit(node):
        if node is None:
            return
        preorder.append(node.val)
        visit(node.left)
        inorder.append(node.val)
        visit(node.right)

    visit(root)
    return preorder, inorder


def _word(rng):
    return "".join(rng.choices("abcd", k=rng.randint(1, 7)))


def _gas_starts(gas, cost):
    valid = []
    for start in range(len(gas)):
        fuel = 0
        for offset in range(len(gas)):
            station = (start + offset) % len(gas)
            fuel += gas[station] - cost[station]
            if fuel < 0:
                break
        else:
            valid.append(start)
    return valid


def generated_args(folder, rng):
    if folder in PER_PROBLEM_FOLDERS:
        path = Path(__file__).resolve().parents[1] / "problems" / folder / "parity.py"
        return validate_generated_payload(metadata(folder), load_parity_generator(path)(rng))
    if folder == "0001-two-sum":
        while True:
            nums = rng.sample(range(-100, 101), rng.randint(2, 15))
            a, b = rng.sample(range(len(nums)), 2)
            target = nums[a] + nums[b]
            if (
                sum(
                    nums[i] + nums[j] == target
                    for i in range(len(nums))
                    for j in range(i + 1, len(nums))
                )
                == 1
            ):
                return [nums, target]
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
        while True:
            s = "".join(rng.choices("aAbBc", k=rng.randint(1, 35)))
            t = "".join(rng.choices("aAbBc", k=rng.randint(1, 6)))
            wanted = Counter(t)
            best = len(s) + 1
            answers = set()
            for left in range(len(s)):
                counts = Counter()
                for right in range(left, len(s)):
                    counts[s[right]] += 1
                    if all(counts[letter] >= count for letter, count in wanted.items()):
                        size = right - left + 1
                        if size < best:
                            best, answers = size, {s[left : right + 1]}
                        elif size == best:
                            answers.add(s[left : right + 1])
                        break
            if len(answers) <= 1:
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
    problem = int(folder.split("-", 1)[0])
    if problem in {42, 11, 121}:
        minimum = 2 if problem == 11 else 1
        return [[rng.randint(0, 100) for _ in range(rng.randint(minimum, 40))]]
    if problem == 152:
        # Every subarray product fits signed int32: 3**12 is safely bounded.
        return [[rng.randint(-3, 3) for _ in range(rng.randint(1, 12))]]
    if problem == 560:
        return [[rng.randint(-10, 10) for _ in range(rng.randint(1, 40))], rng.randint(-40, 40)]
    if problem == 239:
        nums = [rng.randint(-100, 100) for _ in range(rng.randint(1, 40))]
        return [nums, rng.randint(1, len(nums))]
    if problem == 169:
        size = rng.randint(1, 40)
        majority = rng.randint(-20, 20)
        others = [value for value in range(-20, 21) if value != majority]
        nums = [majority] * (size // 2 + 1)
        nums.extend(rng.choices(others, k=size - len(nums)))
        rng.shuffle(nums)
        return [nums]
    if problem == 217:
        return [[rng.randint(-20, 20) for _ in range(rng.randint(1, 40))]]
    if problem == 242:
        first = "".join(rng.choices("abcd", k=rng.randint(1, 35)))
        second = (
            "".join(rng.sample(first, len(first)))
            if rng.random() < 0.5
            else "".join(rng.choices("abcd", k=rng.randint(1, 35)))
        )
        return [first, second]
    if problem == 347:
        values = rng.sample(range(-30, 31), rng.randint(1, 10))
        frequencies = rng.sample(range(1, 21), len(values))
        nums = [
            value
            for value, frequency in zip(values, frequencies, strict=True)
            for _ in range(frequency)
        ]
        rng.shuffle(nums)
        return [nums, rng.randint(1, len(values))]
    if problem == 24:
        return [[rng.randint(0, 100) for _ in range(rng.randint(0, 40))]]
    if problem == 105:
        tree = _random_tree(rng, nonempty=True, unique=True)
        preorder, inorder = _tree_traversals(tree)
        return [preorder, inorder]
    if problem in {112, 543, 94, 104, 199}:
        tree = _random_tree(rng, nonempty=problem == 543)
        if problem != 112:
            return [tree_to_json(tree)]
        leaf_sums = []
        pending = [(tree, 0)] if tree is not None else []
        while pending:
            node, before = pending.pop()
            total = before + node.val
            if node.left is None and node.right is None:
                leaf_sums.append(total)
            for child in (node.left, node.right):
                if child is not None:
                    pending.append((child, total))
        target = (
            rng.choice(leaf_sums) if leaf_sums and rng.random() < 0.5 else rng.randint(-100, 100)
        )
        return [tree_to_json(tree), target]
    if problem == 100:
        first = tree_to_json(_random_tree(rng))
        second = first[:] if rng.random() < 0.5 else tree_to_json(_random_tree(rng))
        return [first, second]
    if problem == 230:
        values = rng.sample(range(1, 1001), rng.randint(1, 25))
        root = TreeNode(values[0])
        for value in values[1:]:
            current = root
            while True:
                side = "left" if value < current.val else "right"
                following = getattr(current, side)
                if following is None:
                    setattr(current, side, TreeNode(value))
                    break
                current = following
        return [tree_to_json(root), rng.randint(1, len(values))]
    if problem == 21:
        return [sorted(rng.randint(-100, 100) for _ in range(rng.randint(0, 30))) for _ in range(2)]
    if problem == 743:
        count = rng.randint(2, 8)
        pairs = [(a, b) for a in range(1, count + 1) for b in range(1, count + 1) if a != b]
        chosen = rng.sample(pairs, rng.randint(1, min(18, len(pairs))))
        return [[[a, b, rng.randint(0, 20)] for a, b in chosen], count, rng.randint(1, count)]
    if problem == 1584:
        points = rng.sample(
            [(x, y) for x in range(-30, 31) for y in range(-30, 31)], rng.randint(1, 15)
        )
        return [[list(point) for point in points]]
    if problem == 547:
        count = rng.randint(1, 10)
        matrix = [[int(i == j) for j in range(count)] for i in range(count)]
        for i in range(count):
            for j in range(i + 1, count):
                matrix[i][j] = matrix[j][i] = int(rng.random() < 0.3)
        return [matrix]
    if problem == 55:
        return [[rng.randint(0, 6) for _ in range(rng.randint(1, 30))]]
    if problem == 134:
        while True:
            count = rng.randint(1, 15)
            gas = [rng.randint(0, 10) for _ in range(count)]
            cost = [rng.randint(0, 10) for _ in range(count)]
            if len(_gas_starts(gas, cost)) <= 1:
                return [gas, cost]
    if problem == 22:
        return [rng.randint(1, 6)]
    if problem == 39:
        return [rng.sample(range(2, 16), rng.randint(1, 6)), rng.randint(1, 30)]
    if problem in {46, 78}:
        limit = 6 if problem == 46 else 8
        return [rng.sample(range(-10, 11), rng.randint(1, limit))]
    if problem == 695:
        rows, columns = rng.randint(1, 6), rng.randint(1, 6)
        return [[[rng.randint(0, 1) for _ in range(columns)] for _ in range(rows)]]
    if problem == 72:
        return ["".join(rng.choices("abcd", k=rng.randint(0, 20))) for _ in range(2)]
    if problem == 518:
        # Small totals also bound intermediate combination counts below INT_MAX.
        return [rng.randint(0, 80), rng.sample(range(1, 21), rng.randint(1, 6))]
    if problem == 416:
        return [[rng.randint(1, 20) for _ in range(rng.randint(1, 18))]]
    if problem == 139:
        words = set()
        while len(words) < 8:
            words.add(_word(rng))
        words = sorted(words)
        text = (
            "".join(rng.choices(words, k=rng.randint(1, 4)))
            if rng.random() < 0.5
            else "".join(rng.choices("abcde", k=rng.randint(1, 25)))
        )
        return [text, words]
    if problem == 201:
        left = rng.randint(0, 1_000_000)
        return [left, left + rng.randint(0, 10_000)]
    if problem == 70:
        return [rng.randint(1, 45)]
    if problem == 746:
        return [[rng.randint(0, 999) for _ in range(rng.randint(2, 30))]]
    if problem == 213:
        return [[rng.randint(0, 100) for _ in range(rng.randint(1, 20))]]
    if problem == 62:
        return [rng.randint(1, 12), rng.randint(1, 12)]
    if problem == 338:
        return [rng.randint(0, 256)]
    if problem == 509:
        return [rng.randint(0, 30)]
    if problem == 71:
        pieces = [
            rng.choice(["", "a", "home", ".", "..", "...", "user1", "b_c", "file.txt"])
            for _ in range(rng.randint(1, 20))
        ]
        return ["/" + "/".join(pieces) + ("/" if rng.random() < 0.5 else "")]
    if problem == 704:
        nums = sorted(rng.sample(range(-100, 101), rng.randint(1, 40)))
        return [nums, rng.choice(nums) if rng.random() < 0.5 else 500]
    if problem == 74:
        rows, columns = rng.randint(1, 6), rng.randint(1, 6)
        nums = sorted(rng.sample(range(-1000, 1001), rows * columns))
        matrix = [nums[index * columns : (index + 1) * columns] for index in range(rows)]
        return [matrix, rng.choice(nums) if rng.random() < 0.5 else 2000]
    if problem == 146:
        operations, arguments = ["LRUCache"], [[rng.randint(1, 5)]]
        for _ in range(50):
            key = rng.randint(0, 10)
            if rng.random() < 0.6:
                operations.append("put")
                arguments.append([key, rng.randint(0, 100)])
            else:
                operations.append("get")
                arguments.append([key])
        return [operations, arguments]
    if problem == 981:
        operations, arguments = ["TimeMap"], [[]]
        timestamp = 0
        for _ in range(50):
            key = rng.choice(["a", "b", "c"])
            if rng.random() < 0.6:
                timestamp += rng.randint(1, 4)
                operations.append("set")
                arguments.append([key, _word(rng), timestamp])
            else:
                operations.append("get")
                arguments.append([key, rng.randint(1, max(1, timestamp + 5))])
        return [operations, arguments]
    if problem == 307:
        values = [rng.randint(-100, 100) for _ in range(rng.randint(1, 25))]
        operations, arguments = ["NumArray"], [[values]]
        for _ in range(50):
            if rng.random() < 0.5:
                operations.append("update")
                arguments.append([rng.randrange(len(values)), rng.randint(-100, 100)])
            else:
                left = rng.randrange(len(values))
                operations.append("sumRange")
                arguments.append([left, rng.randrange(left, len(values))])
        return [operations, arguments]
    if problem == 155:
        operations, arguments = ["MinStack"], [[]]
        depth = 0
        for _ in range(50):
            operation = rng.choice(["push", "pop", "top", "getMin"]) if depth else "push"
            operations.append(operation)
            if operation == "push":
                arguments.append([rng.randint(-100, 100)])
                depth += 1
            else:
                arguments.append([])
                depth -= operation == "pop"
        return [operations, arguments]
    if problem == 208:
        operations, arguments = ["Trie"], [[]]
        inserted = []
        for _ in range(50):
            operation = rng.choice(["insert", "search", "startsWith"])
            word = rng.choice(inserted) if inserted and rng.random() < 0.5 else _word(rng)
            if operation == "startsWith":
                word = word[: rng.randint(1, len(word))]
            if operation == "insert":
                inserted.append(word)
            operations.append(operation)
            arguments.append([word])
        return [operations, arguments]
    if problem == 703:
        k = rng.randint(1, 8)
        values = [rng.randint(-100, 100) for _ in range(rng.randint(k - 1, k + 6))]
        operations, arguments = ["KthLargest"], [[k, values]]
        for _ in range(50):
            operations.append("add")
            arguments.append([rng.randint(-100, 100)])
        return [operations, arguments]
    raise ValueError(f"No generator for {folder}")


@pytest.mark.skipif(
    not os.environ.get("ATLAS_CPP_BIN_DIR"), reason="C++ runners enabled by ATLAS_CPP_BIN_DIR"
)
@pytest.mark.parametrize("folder", FOLDERS)
def test_generated_cpp_python_parity(folder):
    """150 cases per counterpart: 33,750 comparisons across the two language tracks."""
    rng = random.Random(20261012 + int(folder.split("-", 1)[0]))
    meta = metadata(folder)
    cases = [validate_generated_payload(meta, generated_args(folder, rng)) for _ in range(150)]
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
    for index, (line, args) in enumerate(zip(lines, cases, strict=True)):
        actual = json.loads(line)
        expected = (
            evaluate(folder, args=args)
            if meta["kind"] == "method"
            else evaluate(folder, operations=args[0], arguments=args[1])
        )
        if folder == "0001-two-sum":
            # Multiple pairs can be valid; compare the specification rather than pair choice.
            assert isinstance(actual, list) and len(actual) == 2
            assert all(type(i) is int and 0 <= i < len(args[0]) for i in actual)
            assert actual[0] != actual[1]
            assert args[0][actual[0]] + args[0][actual[1]] == args[1]
        else:
            assert check_result(meta, actual, expected, args=args), (
                folder,
                index,
                args,
                actual,
                expected,
            )


def _run_cpp_stress_case(folder, args):
    binary_dir = Path(os.environ["ATLAS_CPP_BIN_DIR"]).resolve()
    suffix = ".exe" if os.name == "nt" else ""
    binary = binary_dir / f"atlas_{folder.replace('-', '_')}{suffix}"
    result = subprocess.run(
        [str(binary)],
        input=json.dumps(args) + "\n",
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    lines = result.stdout.splitlines()
    assert len(lines) == 1, f"{folder}: stress input must produce exactly one result"
    return json.loads(lines[0])


@pytest.mark.skipif(
    not os.environ.get("ATLAS_CPP_BIN_DIR"), reason="C++ runners enabled by ATLAS_CPP_BIN_DIR"
)
def test_cpp_bridges_support_a_hundred_thousand_node_chain():
    """The official maximum-depth shape needs an iterative traversal, not call-stack DFS."""
    size = 100_000
    edges = [[node - 1, node] for node in range(1, size)]
    actual = _run_cpp_stress_case("1192-critical-connections-in-a-network", [size, edges])
    assert isinstance(actual, list) and len(actual) == size - 1
    shape_valid = all(
        isinstance(edge, list) and len(edge) == 2 and all(type(node) is int for node in edge)
        for edge in actual
    )
    assert shape_valid, "Every chain bridge must contain two integer node labels"
    matches = {tuple(sorted(edge)) for edge in actual} == {tuple(edge) for edge in edges}
    assert matches, "Every input edge must be reported exactly once as a bridge"


@pytest.mark.skipif(
    not os.environ.get("ATLAS_CPP_BIN_DIR"), reason="C++ runners enabled by ATLAS_CPP_BIN_DIR"
)
def test_cpp_increasing_path_handles_a_full_size_serpentine_matrix():
    side = 200
    matrix = [
        [row * side + (column if row % 2 == 0 else side - 1 - column) for column in range(side)]
        for row in range(side)
    ]
    assert _run_cpp_stress_case("0329-longest-increasing-path-in-a-matrix", [matrix]) == side**2


@pytest.mark.skipif(
    not os.environ.get("ATLAS_CPP_BIN_DIR"), reason="C++ runners enabled by ATLAS_CPP_BIN_DIR"
)
def test_cpp_parallel_courses_accumulates_the_largest_valid_chain_duration():
    size = 50_000
    prerequisites = [[course - 1, course] for course in range(2, size + 1)]
    actual = _run_cpp_stress_case(
        "2050-parallel-courses-iii", [size, prerequisites, [10_000] * size]
    )
    assert type(actual) is int and actual == 500_000_000


@pytest.mark.skipif(
    not os.environ.get("ATLAS_CPP_BIN_DIR"), reason="C++ runners enabled by ATLAS_CPP_BIN_DIR"
)
@pytest.mark.parametrize(
    "folder",
    [
        "0235-lowest-common-ancestor-of-a-binary-search-tree",
        "0236-lowest-common-ancestor-of-a-binary-tree",
    ],
)
def test_cpp_ancestor_references_preserve_identities_on_a_hundred_thousand_node_tree(folder):
    size = 100_000
    tree = [0]
    for value in range(1, size):
        tree.extend([None, value])
    actual = _run_cpp_stress_case(folder, [tree, size // 2, size - 1])
    assert type(actual) is int and actual == size // 2
    # Each runner also checks that the result is an original node and all labels/links survive.


@pytest.mark.skipif(
    not os.environ.get("ATLAS_CPP_BIN_DIR"), reason="C++ runners enabled by ATLAS_CPP_BIN_DIR"
)
def test_cpp_palindrome_restores_a_hundred_thousand_borrowed_list_nodes():
    half = [index % 10 for index in range(50_000)]
    actual = _run_cpp_stress_case("0234-palindrome-linked-list", [half + half[::-1]])
    assert actual is True
    # The runner validates every original node identity, label and next link after the call.

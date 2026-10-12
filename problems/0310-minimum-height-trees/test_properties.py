import collections
import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0310-minimum-height-trees"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_310", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(n, edges):
    adjacent = [[] for _ in range(n)]
    for first, last in edges:
        adjacent[first].append(last)
        adjacent[last].append(first)
    heights = []
    for start in range(n):
        seen, pending = {start}, collections.deque([(start, 0)])
        height = 0
        while pending:
            node, depth = pending.popleft()
            height = max(height, depth)
            for neighbor in adjacent[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append((neighbor, depth + 1))
        heights.append(height)
    return [index for index, height in enumerate(heights) if height == min(heights)]


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

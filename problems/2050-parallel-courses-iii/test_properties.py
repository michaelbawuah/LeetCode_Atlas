import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "2050-parallel-courses-iii"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_2050", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(n, relations, time):
    adjacent = [[] for _ in range(n)]
    for a, b in relations:
        adjacent[a - 1].append(b - 1)

    def longest(node):
        return time[node] + max((longest(last) for last in adjacent[node]), default=0)

    return max(longest(node) for node in range(n))


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

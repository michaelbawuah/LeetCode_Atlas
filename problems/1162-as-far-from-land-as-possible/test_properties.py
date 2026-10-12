import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "1162-as-far-from-land-as-possible"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_1162", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(grid):
    land = [(r, c) for r in range(len(grid)) for c in range(len(grid)) if grid[r][c]]
    water = [(r, c) for r in range(len(grid)) for c in range(len(grid)) if not grid[r][c]]
    if not land or not water:
        return -1
    return max(min(abs(r - a) + abs(c - b) for a, b in land) for r, c in water)


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

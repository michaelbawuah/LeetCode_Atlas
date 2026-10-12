import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "1020-number-of-enclaves"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_1020", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(grid):
    rows, cols = len(grid), len(grid[0])
    remaining = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c]}
    count = 0
    while remaining:
        start = remaining.pop()
        component = {start}
        pending = [start]
        while pending:
            r, c = pending.pop()
            for cell in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if cell in remaining:
                    remaining.remove(cell)
                    component.add(cell)
                    pending.append(cell)
        if all(r not in (0, rows - 1) and c not in (0, cols - 1) for r, c in component):
            count += len(component)
    return count


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

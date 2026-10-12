import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "1631-path-with-minimum-effort"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_1631", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(heights):
    rows, cols = len(heights), len(heights[0])
    thresholds = {0}
    for r in range(rows):
        for c in range(cols):
            for nr, nc in ((r + 1, c), (r, c + 1)):
                if nr < rows and nc < cols:
                    thresholds.add(abs(heights[r][c] - heights[nr][nc]))
    for limit in sorted(thresholds):
        seen, pending = {(0, 0)}, [(0, 0)]
        while pending:
            r, c = pending.pop()
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in seen
                    and abs(heights[r][c] - heights[nr][nc]) <= limit
                ):
                    seen.add((nr, nc))
                    pending.append((nr, nc))
        if (rows - 1, cols - 1) in seen:
            return limit
    raise AssertionError("Maximum edge threshold must connect the grid")


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

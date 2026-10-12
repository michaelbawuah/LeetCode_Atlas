import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0329-longest-increasing-path-in-a-matrix"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_329", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(matrix):
    rows, cols = len(matrix), len(matrix[0])

    def walk(row, col):
        lengths = [1]
        for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[row][col]:
                lengths.append(1 + walk(nr, nc))
        return max(lengths)

    return max(walk(row, col) for row in range(rows) for col in range(cols))


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

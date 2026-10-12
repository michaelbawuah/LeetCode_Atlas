import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0542-01-matrix"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_542", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(mat):
    zeros = [(r, c) for r in range(len(mat)) for c in range(len(mat[0])) if mat[r][c] == 0]
    return [
        [min(abs(r - zr) + abs(c - zc) for zr, zc in zeros) for c in range(len(mat[0]))]
        for r in range(len(mat))
    ]


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

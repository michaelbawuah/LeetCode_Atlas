import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "2192-all-ancestors-of-a-node-in-a-directed-acyclic-graph"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_2192", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(n, edges):
    reach = [[False] * n for _ in range(n)]
    for a, b in edges:
        reach[a][b] = True
    for via in range(n):
        for a in range(n):
            for b in range(n):
                reach[a][b] |= reach[a][via] and reach[via][b]
    return [[first for first in range(n) if reach[first][last]] for last in range(n)]


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

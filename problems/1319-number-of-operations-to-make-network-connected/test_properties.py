import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "1319-number-of-operations-to-make-network-connected"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_1319", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(n, edges):
    reach = [[i == j for j in range(n)] for i in range(n)]
    for a, b in edges:
        reach[a][b] = reach[b][a] = True
    for via in range(n):
        for a in range(n):
            for b in range(n):
                reach[a][b] |= reach[a][via] and reach[via][b]
    representatives = {min(j for j in range(n) if reach[i][j]) for i in range(n)}
    return len(representatives) - 1 if len(edges) >= n - 1 else -1


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

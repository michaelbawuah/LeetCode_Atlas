import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0841-keys-and-rooms"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_841", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(rooms):
    n = len(rooms)
    reach = [[i == j or j in rooms[i] for j in range(n)] for i in range(n)]
    for via in range(n):
        for first in range(n):
            for last in range(n):
                reach[first][last] |= reach[first][via] and reach[via][last]
    return all(reach[0])


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

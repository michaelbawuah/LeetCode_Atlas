import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0909-snakes-and-ladders"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_909", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(board):
    n = len(board)
    labels = []
    for below in range(n):
        row = board[n - 1 - below]
        labels.extend(row if below % 2 == 0 else row[::-1])
    count = n * n
    distances = [[0 if i == j else 10000 for j in range(count)] for i in range(count)]
    for first in range(1, count + 1):
        for landed in range(first + 1, min(count, first + 6) + 1):
            destination = labels[landed - 1] if labels[landed - 1] != -1 else landed
            distances[first - 1][destination - 1] = min(distances[first - 1][destination - 1], 1)
    for via in range(count):
        for first in range(count):
            for last in range(count):
                distances[first][last] = min(
                    distances[first][last], distances[first][via] + distances[via][last]
                )
    return distances[0][-1] if distances[0][-1] < 10000 else -1


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

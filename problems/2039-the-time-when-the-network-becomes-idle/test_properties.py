import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "2039-the-time-when-the-network-becomes-idle"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_2039", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(edges, patience):
    n = len(patience)
    distance = [[0 if a == b else 1000 for b in range(n)] for a in range(n)]
    for a, b in edges:
        distance[a][b] = distance[b][a] = 1
    for via in range(n):
        for a in range(n):
            for b in range(n):
                distance[a][b] = min(distance[a][b], distance[a][via] + distance[via][b])
    arrivals = []
    for node in range(1, n):
        first_response = 2 * distance[node][0]
        sent = 0
        while sent < first_response:
            arrivals.append(sent + first_response)
            sent += patience[node]
    return max(arrivals) + 1


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

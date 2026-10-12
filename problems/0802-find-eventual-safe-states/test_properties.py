import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0802-find-eventual-safe-states"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_802", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(graph):
    count = len(graph)
    reach = [[last in graph[first] for last in range(count)] for first in range(count)]
    for via in range(count):
        for first in range(count):
            for last in range(count):
                reach[first][last] |= reach[first][via] and reach[via][last]
    return [
        node
        for node in range(count)
        if not any(reach[node][cycle] and reach[cycle][cycle] for cycle in range(count))
    ]


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

import importlib.util
import itertools
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0332-reconstruct-itinerary"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_332", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(tickets):
    routes = []
    for order in itertools.permutations(range(len(tickets))):
        path = ["JFK"]
        for index in order:
            first, last = tickets[index]
            if first != path[-1]:
                break
            path.append(last)
        else:
            routes.append(path)
    return min(routes)


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

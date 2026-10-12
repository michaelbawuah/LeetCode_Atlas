import importlib.util
import itertools
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "2127-maximum-employees-to-be-invited-to-a-meeting"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_2127", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(favorite):
    n = len(favorite)
    for size in range(n, 1, -1):
        for group in itertools.combinations(range(n), size):
            for tail in itertools.permutations(group[1:]):
                circle = (group[0], *tail)
                if all(
                    favorite[node] in (circle[index - 1], circle[(index + 1) % size])
                    for index, node in enumerate(circle)
                ):
                    return size
    return 0


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

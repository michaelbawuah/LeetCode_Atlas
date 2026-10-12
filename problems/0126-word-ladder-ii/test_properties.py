import importlib.util
import itertools
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0126-word-ladder-ii"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_126", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(begin, end, dictionary):
    if end not in dictionary:
        return []
    interior = list(set(dictionary) - {begin, end})
    for length in range(len(interior) + 1):
        found = []
        for middle in itertools.permutations(interior, length):
            path = [begin, *middle, end]
            if all(
                sum(a != b for a, b in zip(first, last, strict=True)) == 1
                for first, last in zip(path, path[1:], strict=False)
            ):
                found.append(path)
        if found:
            return found
    return []


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

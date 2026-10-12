import importlib.util
import itertools
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0797-all-paths-from-source-to-target"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_797", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(graph):
    answers = []
    middle = list(range(1, len(graph) - 1))
    for length in range(len(middle) + 1):
        for interior in itertools.permutations(middle, length):
            path = [0, *interior, len(graph) - 1]
            if all(last in graph[first] for first, last in zip(path, path[1:], strict=False)):
                answers.append(path)
    return answers


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

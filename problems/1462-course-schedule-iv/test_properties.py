import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "1462-course-schedule-iv"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_1462", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(n, edges, queries):
    adjacent = [[] for _ in range(n)]
    for a, b in edges:
        adjacent[a].append(b)
    answers = []
    for first, last in queries:
        seen = set()
        pending = list(adjacent[first])
        while pending:
            node = pending.pop()
            if node not in seen:
                seen.add(node)
                pending.extend(adjacent[node])
        answers.append(last in seen)
    return answers


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

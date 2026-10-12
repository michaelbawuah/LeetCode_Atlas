import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "1192-critical-connections-in-a-network"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_1192", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(n, edges):
    bridges = []
    for removed, edge in enumerate(edges):
        adjacent = [[] for _ in range(n)]
        for index, (a, b) in enumerate(edges):
            if index != removed:
                adjacent[a].append(b)
                adjacent[b].append(a)
        seen, pending = {0}, [0]
        while pending:
            for neighbor in adjacent[pending.pop()]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
        if len(seen) != n:
            bridges.append(edge)
    return bridges


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)


def test_iterative_low_links_handle_the_maximum_depth_without_recursion():
    count = 100_000
    edges = [[index, index + 1] for index in range(count - 1)]
    actual = evaluate(FOLDER, args=[count, edges])
    assert len(actual) == count - 1
    assert {tuple(sorted(edge)) for edge in actual} == {
        (index, index + 1) for index in range(count - 1)
    }

import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0433-minimum-genetic-mutation"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_433", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(start, end, bank):
    if start == end:
        return 0
    if end not in bank:
        return -1
    genes = list(set(bank) | {start})
    distance = [[0 if i == j else 1000 for j in range(len(genes))] for i in range(len(genes))]
    for i, a in enumerate(genes):
        for j, b in enumerate(genes):
            if sum(x != y for x, y in zip(a, b, strict=True)) == 1:
                distance[i][j] = 1
    for via in range(len(genes)):
        for i in range(len(genes)):
            for j in range(len(genes)):
                distance[i][j] = min(distance[i][j], distance[i][via] + distance[via][j])
    answer = distance[genes.index(start)][genes.index(end)]
    return answer if answer < 1000 else -1


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

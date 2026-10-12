import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0947-most-stones-removed-with-same-row-or-column"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_947", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(stones):
    unseen = set(range(len(stones)))
    components = 0
    while unseen:
        pending = [unseen.pop()]
        components += 1
        while pending:
            node = pending.pop()
            linked = {
                other
                for other in unseen
                if stones[node][0] == stones[other][0] or stones[node][1] == stones[other][1]
            }
            unseen.difference_update(linked)
            pending.extend(linked)
    return len(stones) - components


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

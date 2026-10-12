import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0934-shortest-bridge"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_934", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(grid):
    n = len(grid)
    unseen = {(r, c) for r in range(n) for c in range(n) if grid[r][c]}
    components = []
    while unseen:
        start = unseen.pop()
        component = {start}
        pending = [start]
        while pending:
            r, c = pending.pop()
            for cell in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if cell in unseen:
                    unseen.remove(cell)
                    component.add(cell)
                    pending.append(cell)
        components.append(component)
    return min(abs(r - a) + abs(c - b) - 1 for r, c in components[0] for a, b in components[1])


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

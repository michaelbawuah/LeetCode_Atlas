import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0959-regions-cut-by-slashes"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_959", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(grid):
    n = len(grid) * 3
    blocked = set()
    for row, text in enumerate(grid):
        for col, character in enumerate(text):
            if character == "/":
                blocked.update((row * 3 + offset, col * 3 + 2 - offset) for offset in range(3))
            elif character == chr(92):
                blocked.update((row * 3 + offset, col * 3 + offset) for offset in range(3))
    empty = {(r, c) for r in range(n) for c in range(n)} - blocked
    regions = 0
    while empty:
        pending = [empty.pop()]
        regions += 1
        while pending:
            r, c = pending.pop()
            for cell in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if cell in empty:
                    empty.remove(cell)
                    pending.append(cell)
    return regions


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

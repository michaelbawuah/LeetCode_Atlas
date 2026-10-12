import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "1254-number-of-closed-islands"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_1254", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(grid):
    rows, cols = len(grid), len(grid[0])
    outside = rows * cols
    parent = list(range(outside + 1))

    def root(node):
        while parent[node] != node:
            node = parent[node]
        return node

    def join(a, b):
        parent[root(a)] = root(b)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                cell = r * cols + c
                if r in (0, rows - 1) or c in (0, cols - 1):
                    join(cell, outside)
                for nr, nc in ((r + 1, c), (r, c + 1)):
                    if nr < rows and nc < cols and grid[nr][nc] == 0:
                        join(cell, nr * cols + nc)
    return len(
        {
            root(r * cols + c)
            for r in range(rows)
            for c in range(cols)
            if grid[r][c] == 0 and root(r * cols + c) != root(outside)
        }
    )


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "1926-nearest-exit-from-entrance-in-maze"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_1926", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(maze, entrance):
    rows, cols = len(maze), len(maze[0])
    cells = [(r, c) for r in range(rows) for c in range(cols) if maze[r][c] == "."]
    n = len(cells)
    distances = [[0 if i == j else 1000 for j in range(n)] for i in range(n)]
    for i, (r, c) in enumerate(cells):
        for j, (a, b) in enumerate(cells):
            if abs(r - a) + abs(c - b) == 1:
                distances[i][j] = 1
    for via in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][via] + distances[via][j])
    start = cells.index(tuple(entrance))
    exits = [
        i
        for i, (r, c) in enumerate(cells)
        if i != start and (r in (0, rows - 1) or c in (0, cols - 1))
    ]
    answer = min((distances[start][i] for i in exits), default=1000)
    return answer if answer < 1000 else -1


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

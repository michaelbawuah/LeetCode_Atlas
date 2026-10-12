from copy import deepcopy

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0994-rotting-oranges"


@st.composite
def orange_grids(draw):
    rows, cols = draw(st.integers(1, 5)), draw(st.integers(1, 5))
    cells = draw(st.lists(st.integers(0, 2), min_size=rows * cols, max_size=rows * cols))
    return [cells[row * cols : (row + 1) * cols] for row in range(rows)]


def synchronous_spread(original):
    grid = deepcopy(original)
    rows, cols = len(grid), len(grid[0])
    minutes = 0
    while any(1 in row for row in grid):
        newly_rotten = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and any(
                    0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2
                    for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
                ):
                    newly_rotten.append((row, col))
        if not newly_rotten:
            return -1
        for row, col in newly_rotten:
            grid[row][col] = 2
        minutes += 1
    return minutes


@given(orange_grids())
def test_breadth_first_spread_matches_synchronous_full_grid_updates(grid):
    assert evaluate(FOLDER, args=[grid]) == synchronous_spread(grid)

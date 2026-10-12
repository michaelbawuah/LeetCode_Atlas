from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0200-number-of-islands"


@st.composite
def grids(draw):
    rows = draw(st.integers(1, 8))
    cols = draw(st.integers(1, 8))
    values = draw(st.lists(st.booleans(), min_size=rows * cols, max_size=rows * cols))
    return [
        ["1" if values[row * cols + col] else "0" for col in range(cols)] for row in range(rows)
    ]


def union_find_count(grid):
    rows, cols = len(grid), len(grid[0])
    parent = {
        (row, col): (row, col)
        for row in range(rows)
        for col in range(cols)
        if grid[row][col] == "1"
    }

    def find(cell):
        while parent[cell] != cell:
            cell = parent[cell]
        return cell

    for row, col in parent:
        for neighbor in ((row + 1, col), (row, col + 1)):
            if neighbor in parent:
                first, second = find((row, col)), find(neighbor)
                if first != second:
                    parent[first] = second
    return len({find(cell) for cell in parent})


@given(grids())
def test_flood_fill_matches_disjoint_sets(grid):
    assert evaluate(FOLDER, args=[grid]) == union_find_count(grid)

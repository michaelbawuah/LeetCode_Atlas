from collections import Counter

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0695-max-area-of-island"


@st.composite
def binary_grids(draw):
    rows, cols = draw(st.integers(1, 7)), draw(st.integers(1, 7))
    cells = draw(st.lists(st.integers(0, 1), min_size=rows * cols, max_size=rows * cols))
    return [cells[row * cols : (row + 1) * cols] for row in range(rows)]


def union_find_area(grid):
    parent = {
        (row, col): (row, col)
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == 1
    }

    def root(cell):
        while parent[cell] != cell:
            cell = parent[cell]
        return cell

    for row, col in parent:
        for neighbor in ((row + 1, col), (row, col + 1)):
            if neighbor in parent:
                first, second = root((row, col)), root(neighbor)
                if first != second:
                    parent[first] = second
    sizes = Counter(root(cell) for cell in parent)
    return max(sizes.values(), default=0)


@given(binary_grids())
def test_flood_fill_area_matches_component_sizes_from_union_find(grid):
    assert evaluate(FOLDER, args=[grid]) == union_find_area(grid)

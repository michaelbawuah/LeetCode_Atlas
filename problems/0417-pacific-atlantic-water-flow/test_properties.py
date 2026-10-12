from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0417-pacific-atlantic-water-flow"


@st.composite
def terrains(draw):
    rows, cols = draw(st.integers(1, 5)), draw(st.integers(1, 5))
    cells = draw(st.lists(st.integers(0, 20), min_size=rows * cols, max_size=rows * cols))
    return [cells[row * cols : (row + 1) * cols] for row in range(rows)]


def downhill_oceans(heights, start):
    rows, cols = len(heights), len(heights[0])
    seen, pending = {start}, [start]
    pacific = atlantic = False
    while pending:
        row, col = pending.pop()
        pacific |= row == 0 or col == 0
        atlantic |= row == rows - 1 or col == cols - 1
        for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and (nr, nc) not in seen
                and heights[nr][nc] <= heights[row][col]
            ):
                seen.add((nr, nc))
                pending.append((nr, nc))
    return pacific and atlantic


@given(terrains())
def test_reverse_ocean_search_matches_each_cells_forward_flow(heights):
    expected = {
        (row, col)
        for row in range(len(heights))
        for col in range(len(heights[0]))
        if downhill_oceans(heights, (row, col))
    }
    actual = evaluate(FOLDER, args=[heights])
    assert len(actual) == len(expected)
    assert {tuple(cell) for cell in actual} == expected

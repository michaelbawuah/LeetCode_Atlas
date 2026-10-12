from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0063-unique-paths-ii"


def oracle(grid):
    def walk(row, column):
        if row >= len(grid) or column >= len(grid[0]) or grid[row][column]:
            return 0
        if row == len(grid) - 1 and column == len(grid[0]) - 1:
            return 1
        return walk(row + 1, column) + walk(row, column + 1)

    return walk(0, 0)


@st.composite
def rectangular(draw, cells, maximum):
    rows, columns = draw(st.integers(1, maximum)), draw(st.integers(1, maximum))
    values = draw(st.lists(cells, min_size=rows * columns, max_size=rows * columns))
    return ([values[index : index + columns] for index in range(0, len(values), columns)],)


@settings(max_examples=60, deadline=None)
@given(rectangular(st.integers(0, 1), 6))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

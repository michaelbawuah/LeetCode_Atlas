from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0064-minimum-path-sum"


def oracle(grid):
    def routes(row, column, total):
        total += grid[row][column]
        if row == len(grid) - 1 and column == len(grid[0]) - 1:
            return total
        results = []
        if row + 1 < len(grid):
            results.append(routes(row + 1, column, total))
        if column + 1 < len(grid[0]):
            results.append(routes(row, column + 1, total))
        return min(results)

    return routes(0, 0, 0)


@st.composite
def rectangular(draw, cells, maximum):
    rows, columns = draw(st.integers(1, maximum)), draw(st.integers(1, maximum))
    values = draw(st.lists(cells, min_size=rows * columns, max_size=rows * columns))
    return ([values[index : index + columns] for index in range(0, len(values), columns)],)


@settings(max_examples=60, deadline=None)
@given(rectangular(st.integers(0, 20), 5))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

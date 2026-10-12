from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0221-maximal-square"


def oracle(matrix):
    best = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            for side in range(1, min(len(matrix) - row, len(matrix[0]) - column) + 1):
                if all(
                    matrix[r][c] == "1"
                    for r in range(row, row + side)
                    for c in range(column, column + side)
                ):
                    best = max(best, side * side)
    return best


@st.composite
def rectangular(draw, cells, maximum):
    rows, columns = draw(st.integers(1, maximum)), draw(st.integers(1, maximum))
    values = draw(st.lists(cells, min_size=rows * columns, max_size=rows * columns))
    return ([values[index : index + columns] for index in range(0, len(values), columns)],)


@settings(max_examples=60, deadline=None)
@given(rectangular(st.sampled_from("01"), 5))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0931-minimum-falling-path-sum"


def oracle(matrix):
    def fall(row, column):
        if row == len(matrix) - 1:
            return matrix[row][column]
        return matrix[row][column] + min(
            fall(row + 1, following)
            for following in range(max(0, column - 1), min(len(matrix), column + 2))
        )

    return min(fall(0, column) for column in range(len(matrix)))


@st.composite
def squares(draw):
    size = draw(st.integers(1, 5))
    values = draw(st.lists(st.integers(-20, 20), min_size=size * size, max_size=size * size))
    return ([values[index : index + size] for index in range(0, len(values), size)],)


@settings(max_examples=60, deadline=None)
@given(squares())
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

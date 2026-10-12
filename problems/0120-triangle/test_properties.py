from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0120-triangle"


def oracle(triangle):
    def descend(row, column):
        if row == len(triangle) - 1:
            return triangle[row][column]
        return triangle[row][column] + min(descend(row + 1, column), descend(row + 1, column + 1))

    return descend(0, 0)


@st.composite
def triangles(draw):
    height = draw(st.integers(1, 7))
    return (
        [
            draw(st.lists(st.integers(-20, 20), min_size=row, max_size=row))
            for row in range(1, height + 1)
        ],
    )


@settings(max_examples=60, deadline=None)
@given(triangles())
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

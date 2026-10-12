from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0240-search-a-2d-matrix-ii").Solution


@given(st.integers(1, 6), st.integers(1, 6), st.integers(-40, 100), st.data())
def test_staircase_matches_full_membership_scan(rows, columns, target, data):
    matrix = [[0] * columns for _ in range(rows)]
    increments = data.draw(
        st.lists(st.integers(0, 8), min_size=rows * columns, max_size=rows * columns)
    )
    for row in range(rows):
        for column in range(columns):
            above = matrix[row - 1][column] if row else -40
            before = matrix[row][column - 1] if column else -40
            matrix[row][column] = max(above, before) + increments[row * columns + column]
    assert Solution().searchMatrix(matrix, target) == any(target in row for row in matrix)

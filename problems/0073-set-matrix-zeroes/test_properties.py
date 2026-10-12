from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0073-set-matrix-zeroes").Solution


@st.composite
def matrices(draw):
    rows, columns = draw(st.integers(1, 6)), draw(st.integers(1, 6))
    values = draw(st.lists(st.integers(-2, 2), min_size=rows * columns, max_size=rows * columns))
    return [values[row * columns : (row + 1) * columns] for row in range(rows)]


@given(matrices())
def test_matches_original_zero_coordinates_without_cascading(matrix):
    original = [row.copy() for row in matrix]
    identity, row_identities = id(matrix), [id(row) for row in matrix]
    zero_rows = {row for row in range(len(original)) if 0 in original[row]}
    zero_columns = {
        column
        for column in range(len(original[0]))
        if any(original[row][column] == 0 for row in range(len(original)))
    }
    expected = [
        [
            0 if row in zero_rows or column in zero_columns else value
            for column, value in enumerate(values)
        ]
        for row, values in enumerate(original)
    ]
    assert Solution().setZeroes(matrix) is None
    assert matrix == expected
    assert id(matrix) == identity
    assert [id(row) for row in matrix] == row_identities


def test_new_zeroes_must_not_trigger_additional_rows():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0048-rotate-image").Solution


@st.composite
def square_matrices(draw):
    size = draw(st.integers(1, 6))
    values = draw(st.lists(st.integers(-30, 30), min_size=size * size, max_size=size * size))
    return [values[row * size : (row + 1) * size] for row in range(size)]


@given(square_matrices())
def test_in_place_rotation_matches_coordinate_mapping(matrix):
    original = [row.copy() for row in matrix]
    identity, row_identities = id(matrix), [id(row) for row in matrix]
    size = len(matrix)
    expected = [[original[size - 1 - column][row] for column in range(size)] for row in range(size)]
    assert Solution().rotate(matrix) is None
    assert matrix == expected
    assert id(matrix) == identity
    assert [id(row) for row in matrix] == row_identities


@given(square_matrices())
def test_four_rotations_restore_the_original(matrix):
    original = [row.copy() for row in matrix]
    for _ in range(4):
        Solution().rotate(matrix)
    assert matrix == original

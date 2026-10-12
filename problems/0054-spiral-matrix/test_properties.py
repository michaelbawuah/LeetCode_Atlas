from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0054-spiral-matrix").Solution


@st.composite
def matrices(draw):
    rows, columns = draw(st.integers(1, 6)), draw(st.integers(1, 6))
    values = draw(
        st.lists(st.integers(-100, 100), min_size=rows * columns, max_size=rows * columns)
    )
    return [values[row * columns : (row + 1) * columns] for row in range(rows)]


def walking_oracle(matrix):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    row = column = direction = 0
    result = []
    for _ in range(len(matrix) * len(matrix[0])):
        result.append(matrix[row][column])
        visited.add((row, column))
        dr, dc = moves[direction]
        following = row + dr, column + dc
        if not (
            0 <= following[0] < len(matrix)
            and 0 <= following[1] < len(matrix[0])
            and following not in visited
        ):
            direction = (direction + 1) % 4
            dr, dc = moves[direction]
        row, column = row + dr, column + dc
    return result


@given(matrices())
def test_matches_directional_walk_without_mutating_input(matrix):
    original = [row.copy() for row in matrix]
    assert Solution().spiralOrder(matrix) == walking_oracle(original)
    assert matrix == original

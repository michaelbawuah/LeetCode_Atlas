from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0036-valid-sudoku").Solution


def oracle(board):
    units = list(board) + [list(column) for column in zip(*board, strict=True)]
    for top in range(0, 9, 3):
        for left in range(0, 9, 3):
            units.append(
                [
                    board[row][column]
                    for row in range(top, top + 3)
                    for column in range(left, left + 3)
                ]
            )
    return all(
        len([value for value in unit if value != "."])
        == len({value for value in unit if value != "."})
        for unit in units
    )


@given(st.dictionaries(st.integers(0, 80), st.sampled_from("123456789"), max_size=20))
def test_sparse_boards_match_independent_unit_validation(cells):
    board = [["."] * 9 for _ in range(9)]
    for index, value in cells.items():
        board[index // 9][index % 9] = value
    assert Solution().isValidSudoku(board) == oracle(board)


@given(st.sets(st.integers(0, 80), max_size=81))
def test_removing_cells_from_a_completed_grid_preserves_validity(holes):
    board = [
        [str((row * 3 + row // 3 + column) % 9 + 1) for column in range(9)] for row in range(9)
    ]
    for index in holes:
        board[index // 9][index % 9] = "."
    assert Solution().isValidSudoku(board)

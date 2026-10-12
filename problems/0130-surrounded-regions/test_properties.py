from copy import deepcopy

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate, load_module

FOLDER = "0130-surrounded-regions"


@st.composite
def boards(draw):
    rows, cols = draw(st.integers(1, 6)), draw(st.integers(1, 6))
    cells = draw(st.lists(st.sampled_from("XO"), min_size=rows * cols, max_size=rows * cols))
    return [cells[row * cols : (row + 1) * cols] for row in range(rows)]


def independently_classify_cells(original):
    rows, cols = len(original), len(original[0])
    result = deepcopy(original)
    for start_row in range(rows):
        for start_col in range(cols):
            if original[start_row][start_col] != "O":
                continue
            seen, pending = {(start_row, start_col)}, [(start_row, start_col)]
            escapes = False
            while pending:
                row, col = pending.pop()
                escapes |= row in (0, rows - 1) or col in (0, cols - 1)
                for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and original[nr][nc] == "O"
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        pending.append((nr, nc))
            if not escapes:
                result[start_row][start_col] = "X"
    return result


@given(boards())
def test_border_protection_matches_independent_escape_search_from_each_cell(board):
    assert evaluate(FOLDER, args=[board]) == independently_classify_cells(board)


def test_platform_method_mutates_the_board_and_returns_none():
    board = [list("XXX"), list("XOX"), list("XXX")]
    assert load_module(FOLDER).Solution().solve(board) is None
    assert board == [list("XXX"), list("XXX"), list("XXX")]

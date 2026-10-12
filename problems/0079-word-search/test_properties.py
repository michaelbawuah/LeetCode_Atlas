from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0079-word-search").Solution


def oracle(board, word):
    rows, cols = len(board), len(board[0])
    paths = [
        ((r, c), frozenset([(r, c)]))
        for r in range(rows)
        for c in range(cols)
        if board[r][c] == word[0]
    ]
    for letter in word[1:]:
        next_paths = []
        for (r, c), used in paths:
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in used
                    and board[nr][nc] == letter
                ):
                    next_paths.append(((nr, nc), used | {(nr, nc)}))
        paths = next_paths
    return bool(paths)


@given(
    rows=st.integers(1, 3),
    cols=st.integers(1, 3),
    word=st.text(alphabet="ab", min_size=1, max_size=6),
    data=st.data(),
)
def test_search_matches_explicit_path_frontier(rows, cols, word, data):
    board = data.draw(
        st.lists(
            st.lists(st.sampled_from(list("ab")), min_size=cols, max_size=cols),
            min_size=rows,
            max_size=rows,
        )
    )
    snapshot = [list(row) for row in board]
    assert Solution().exist(board, word) == oracle(board, word)
    assert board == snapshot

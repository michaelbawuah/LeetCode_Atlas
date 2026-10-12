from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0212-word-search-ii").Solution


def possible(board, word):
    def enumerate_paths(path):
        if len(path) == len(word):
            return True
        row, col = path[-1]
        return any(
            enumerate_paths(path + [(r, c)])
            for r, c in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1))
            if 0 <= r < len(board)
            and 0 <= c < len(board[0])
            and (r, c) not in path
            and board[r][c] == word[len(path)]
        )

    return any(
        enumerate_paths([(r, c)])
        for r in range(len(board))
        for c in range(len(board[0]))
        if board[r][c] == word[0]
    )


@given(
    rows=st.integers(1, 3),
    cols=st.integers(1, 3),
    words=st.lists(
        st.text(alphabet="ab", min_size=1, max_size=5), min_size=1, max_size=12, unique=True
    ),
    data=st.data(),
)
def test_trie_matches_independent_single_word_paths(rows, cols, words, data):
    board = data.draw(
        st.lists(
            st.lists(st.sampled_from(list("ab")), min_size=cols, max_size=cols),
            min_size=rows,
            max_size=rows,
        )
    )
    snapshot = [list(row) for row in board]
    actual = Solution().findWords(board, words)
    expected = {word for word in words if possible(board, word)}
    assert len(actual) == len(set(actual))
    assert set(actual) == expected
    assert board == snapshot

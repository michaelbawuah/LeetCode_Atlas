from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Trie = load_module("0208-implement-trie-prefix-tree").Trie
words = st.text(alphabet="abc", min_size=1, max_size=10)


@given(
    st.lists(
        st.tuples(st.sampled_from(["insert", "search", "prefix"]), words), min_size=1, max_size=80
    )
)
def test_operation_sequence_matches_word_set(actions):
    trie = Trie()
    stored = set()
    for operation, word in actions:
        if operation == "insert":
            assert trie.insert(word) is None
            stored.add(word)
            assert trie.search(word) is True
        elif operation == "search":
            assert trie.search(word) == (word in stored)
        else:
            assert trie.startsWith(word) == any(candidate.startswith(word) for candidate in stored)
    for word in stored:
        assert trie.search(word) is True
        for end in range(1, len(word) + 1):
            assert trie.startsWith(word[:end]) is True

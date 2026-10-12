from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

WordDictionary = load_module("0211-design-add-and-search-words-data-structure").WordDictionary
words = st.text(alphabet="abc", min_size=1, max_size=10)


@given(actions=st.lists(st.tuples(st.booleans(), words), min_size=1, max_size=70), data=st.data())
def test_dictionary_sequence_matches_direct_pattern_checks(actions, data):
    dictionary = WordDictionary()
    stored = set()
    for add_word, text in actions:
        if add_word:
            assert dictionary.addWord(text) is None
            stored.add(text)
            assert dictionary.search(text) is True
        else:
            wildcard_indexes = data.draw(
                st.sets(st.integers(0, len(text) - 1), max_size=min(2, len(text)))
            )
            pattern = "".join(
                "." if index in wildcard_indexes else letter for index, letter in enumerate(text)
            )
            expected = any(
                len(candidate) == len(pattern)
                and all(
                    pattern_letter == "." or pattern_letter == letter
                    for pattern_letter, letter in zip(pattern, candidate, strict=True)
                )
                for candidate in stored
            )
            assert dictionary.search(pattern) == expected
    for word in stored:
        assert dictionary.search(word) is True

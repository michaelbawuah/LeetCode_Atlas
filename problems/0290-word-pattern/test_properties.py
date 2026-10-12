from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0290-word-pattern").Solution


@given(
    pattern=st.text(alphabet="abc", min_size=1, max_size=10),
    words=st.lists(st.sampled_from(["dog", "cat", "fish"]), min_size=1, max_size=10),
)
def test_pattern_matches_pairwise_word_equivalence(pattern, words):
    expected = len(pattern) == len(words) and all(
        (pattern[i] == pattern[j]) == (words[i] == words[j])
        for i in range(len(pattern))
        for j in range(len(pattern))
    )
    assert Solution().wordPattern(pattern, " ".join(words)) == expected

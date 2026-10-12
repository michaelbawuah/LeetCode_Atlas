from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0242-valid-anagram").Solution
words = st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1, max_size=40)


@given(words, words)
def test_matches_sorting_oracle(first, second):
    assert Solution().isAnagram(first, second) == (sorted(first) == sorted(second))


@given(words)
def test_reverse_is_an_anagram_but_extra_character_is_not(word):
    assert Solution().isAnagram(word, word[::-1])
    assert not Solution().isAnagram(word, word + "a")

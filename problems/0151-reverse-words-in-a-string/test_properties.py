import re

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0151-reverse-words-in-a-string").Solution


@given(
    words=st.lists(st.text(alphabet="abc012", min_size=1, max_size=10), min_size=1, max_size=12),
    spaces=st.integers(1, 5),
)
def test_word_reversal_matches_regex_tokens(words, spaces):
    text = "  " + (" " * spaces).join(words) + " "
    tokens = re.findall(r"[^ ]+", text)
    assert Solution().reverseWords(text) == " ".join(tokens[::-1])

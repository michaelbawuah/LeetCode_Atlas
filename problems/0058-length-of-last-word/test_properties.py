from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0058-length-of-last-word").Solution


@given(
    words=st.lists(st.text(alphabet="abcXYZ", min_size=1, max_size=20), min_size=1, max_size=10),
    leading=st.integers(0, 6),
    trailing=st.integers(0, 6),
)
def test_last_word_matches_token_reference(words, leading, trailing):
    text = " " * leading + "  ".join(words) + " " * trailing
    assert Solution().lengthOfLastWord(text) == len(text.split()[-1])

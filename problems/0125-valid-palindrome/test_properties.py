import re
import string

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0125-valid-palindrome").Solution


@given(
    st.text(
        alphabet=string.ascii_letters + string.digits + string.punctuation + " ",
        min_size=1,
        max_size=60,
    )
)
def test_matches_normalized_reverse(s):
    normalized = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    assert Solution().isPalindrome(s) == (normalized == normalized[::-1])


@given(st.text(alphabet=string.ascii_letters + string.digits, min_size=1, max_size=20))
def test_mirrored_text_with_punctuation_is_a_palindrome(s):
    assert Solution().isPalindrome(s + " ,:! " + s[::-1])

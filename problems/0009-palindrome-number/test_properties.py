from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0009-palindrome-number").Solution


@given(st.integers(-(2**31), 2**31 - 1))
def test_half_reversal_matches_text_palindrome(x):
    text = str(x)
    assert Solution().isPalindrome(x) == (text == text[::-1])

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0007-reverse-integer").Solution


@given(st.integers(-(2**31), 2**31 - 1))
def test_digits_match_string_reference(x):
    expected = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
    if not -(2**31) <= expected < 2**31:
        expected = 0
    assert Solution().reverse(x) == expected

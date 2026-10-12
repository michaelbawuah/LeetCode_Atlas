from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0067-add-binary").Solution


@given(a=st.integers(0, 2**100), b=st.integers(0, 2**100))
def test_digit_addition_matches_integer_arithmetic(a, b):
    assert Solution().addBinary(bin(a)[2:], bin(b)[2:]) == bin(a + b)[2:]

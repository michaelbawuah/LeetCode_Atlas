from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0012-integer-to-roman").Solution

THOUSANDS = ["", "M", "MM", "MMM"]
HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


def roman_reference(n):
    return THOUSANDS[n // 1000] + HUNDREDS[n // 100 % 10] + TENS[n // 10 % 10] + ONES[n % 10]


@given(st.integers(1, 3999))
def test_greedy_symbols_match_decimal_place_tables(n):
    assert Solution().intToRoman(n) == roman_reference(n)

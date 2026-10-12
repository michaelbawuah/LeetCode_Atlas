from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0171-excel-sheet-column-number").Solution


def encode(number):
    result = ""
    while number:
        number, digit = divmod(number - 1, 26)
        result = chr(65 + digit) + result
    return result


@given(st.integers(1, 2**31 - 1))
def test_column_number_matches_bijective_encoding(number):
    assert Solution().titleToNumber(encode(number)) == number

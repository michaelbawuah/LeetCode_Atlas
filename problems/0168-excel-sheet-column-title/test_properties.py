from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0168-excel-sheet-column-title").Solution


@given(st.integers(1, 2**31 - 1))
def test_bijective_digits_reconstruct_number(number):
    title = Solution().convertToTitle(number)
    expected = 0
    for letter in title:
        expected = expected * 26 + ord(letter) - ord("A") + 1
    assert expected == number
    assert title and all("A" <= letter <= "Z" for letter in title)

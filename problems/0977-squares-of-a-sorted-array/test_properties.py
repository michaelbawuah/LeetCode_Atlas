from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0977-squares-of-a-sorted-array").Solution


@given(st.lists(st.integers(-10000, 10000), min_size=1, max_size=50))
def test_reverse_fill_matches_full_sort_of_squares(values):
    nums = sorted(values)
    assert Solution().sortedSquares(nums) == sorted(value * value for value in values)

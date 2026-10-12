from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0414-third-maximum-number").Solution


@given(st.lists(st.integers(-2147483648, 2147483647), min_size=1, max_size=60))
def test_three_extrema_match_distinct_full_sort(nums):
    ordered = sorted(set(nums), reverse=True)
    expected = ordered[2] if len(ordered) >= 3 else ordered[0]
    assert Solution().thirdMax(nums) == expected

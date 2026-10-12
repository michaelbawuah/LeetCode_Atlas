from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0053-maximum-subarray").Solution


@given(st.lists(st.integers(-20, 20), min_size=1, max_size=20))
def test_matches_all_nonempty_contiguous_slices(nums):
    expected = max(
        sum(nums[left:right])
        for left in range(len(nums))
        for right in range(left + 1, len(nums) + 1)
    )
    assert Solution().maxSubArray(nums) == expected


@given(st.lists(st.integers(-100, -1), min_size=1, max_size=20))
def test_all_negative_input_requires_a_nonempty_answer(nums):
    assert Solution().maxSubArray(nums) == max(nums)

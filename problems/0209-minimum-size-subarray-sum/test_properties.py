from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0209-minimum-size-subarray-sum").Solution


@given(st.integers(1, 100), st.lists(st.integers(1, 20), min_size=1, max_size=20))
def test_matches_all_contiguous_slices(target, nums):
    lengths = [
        right - left
        for left in range(len(nums))
        for right in range(left + 1, len(nums) + 1)
        if sum(nums[left:right]) >= target
    ]
    assert Solution().minSubArrayLen(target, nums) == min(lengths, default=0)


@given(st.lists(st.integers(1, 20), min_size=1, max_size=20))
def test_total_sum_and_unreachable_thresholds(nums):
    assert Solution().minSubArrayLen(sum(nums), nums) == len(nums)
    assert Solution().minSubArrayLen(sum(nums) + 1, nums) == 0

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0560-subarray-sum-equals-k").Solution


@given(st.lists(st.integers(-5, 5), min_size=1, max_size=20), st.integers(-20, 20))
def test_matches_enumerated_slices_including_negative_values(nums, target):
    expected = sum(
        sum(nums[left:right]) == target
        for left in range(len(nums))
        for right in range(left + 1, len(nums) + 1)
    )
    assert Solution().subarraySum(nums, target) == expected
    assert Solution().subarraySum(nums[::-1], target) == expected


@given(st.integers(1, 100))
def test_zero_arrays_count_every_nonempty_subarray(size):
    assert Solution().subarraySum([0] * size, 0) == size * (size + 1) // 2

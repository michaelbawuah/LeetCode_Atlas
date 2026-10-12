from hypothesis import assume, given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0162-find-peak-element").Solution


@given(st.lists(st.integers(-100, 100), min_size=1, max_size=80))
def test_returned_index_is_any_strict_peak(nums):
    assume(all(first != second for first, second in zip(nums, nums[1:], strict=False)))
    peaks = [
        index
        for index, value in enumerate(nums)
        if (index == 0 or value > nums[index - 1])
        and (index + 1 == len(nums) or value > nums[index + 1])
    ]
    answer = Solution().findPeakElement(nums)
    assert type(answer) is int and answer in peaks

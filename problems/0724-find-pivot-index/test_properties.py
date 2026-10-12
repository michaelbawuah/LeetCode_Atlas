from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0724-find-pivot-index").Solution


@given(st.lists(st.integers(-100, 100), min_size=1, max_size=50))
def test_prefix_pivot_matches_independent_left_right_slice_sums(nums):
    expected = next(
        (index for index in range(len(nums)) if sum(nums[:index]) == sum(nums[index + 1 :])), -1
    )
    assert Solution().pivotIndex(nums) == expected

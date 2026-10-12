from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0525-contiguous-array").Solution


@given(st.lists(st.integers(0, 1), min_size=1, max_size=25))
def test_prefix_balances_match_every_slice_count(nums):
    expected = max(
        (
            right - left
            for left in range(len(nums))
            for right in range(left + 1, len(nums) + 1)
            if nums[left:right].count(0) == nums[left:right].count(1)
        ),
        default=0,
    )
    assert Solution().findMaxLength(nums) == expected

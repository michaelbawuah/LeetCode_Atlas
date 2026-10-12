from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0164-maximum-gap").Solution


@given(st.lists(st.integers(0, 1000000000), min_size=1, max_size=60))
def test_linear_buckets_match_sorted_adjacent_differences(nums):
    ordered = sorted(nums)
    expected = max(
        (second - first for first, second in zip(ordered, ordered[1:], strict=False)), default=0
    )
    assert Solution().maximumGap(nums) == expected

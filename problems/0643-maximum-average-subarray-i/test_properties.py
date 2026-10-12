import math

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0643-maximum-average-subarray-i").Solution


@given(st.lists(st.integers(-10000, 10000), min_size=1, max_size=30), st.data())
def test_rolling_average_matches_independently_summed_windows(nums, data):
    width = data.draw(st.integers(1, len(nums)))
    expected = max(
        sum(nums[start : start + width]) / width for start in range(len(nums) - width + 1)
    )
    assert math.isclose(
        Solution().findMaxAverage(nums, width), expected, rel_tol=1e-9, abs_tol=1e-12
    )

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0239-sliding-window-maximum").Solution


@given(st.lists(st.integers(-100, 100), min_size=1, max_size=35), st.data())
def test_matches_independent_window_maxima_and_reversal(nums, data):
    width = data.draw(st.integers(1, len(nums)))
    expected = [max(nums[start : start + width]) for start in range(len(nums) - width + 1)]
    assert Solution().maxSlidingWindow(nums, width) == expected
    assert Solution().maxSlidingWindow(nums[::-1], width) == expected[::-1]


def test_equal_values_keep_a_nonexpired_maximum():
    assert Solution().maxSlidingWindow([4, 4, 4, 1], 2) == [4, 4, 4]

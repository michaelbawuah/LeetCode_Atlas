from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0042-trapping-rain-water").Solution


@given(st.lists(st.integers(0, 100), min_size=1, max_size=25))
def test_matches_independent_per_bar_left_and_right_maxima(height):
    expected = sum(
        min(max(height[: index + 1]), max(height[index:])) - value
        for index, value in enumerate(height)
    )
    assert Solution().trap(height) == expected
    assert Solution().trap(height[::-1]) == expected


@given(st.lists(st.integers(0, 100), min_size=1, max_size=25), st.integers(0, 10))
def test_height_scaling_scales_volume(height, factor):
    assert Solution().trap([value * factor for value in height]) == factor * Solution().trap(height)

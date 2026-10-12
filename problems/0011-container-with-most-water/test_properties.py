from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0011-container-with-most-water").Solution


@given(st.lists(st.integers(0, 100), min_size=2, max_size=18))
def test_matches_all_pairs(height):
    expected = max(
        (right - left) * min(height[left], height[right])
        for left in range(len(height))
        for right in range(left + 1, len(height))
    )
    assert Solution().maxArea(height) == expected


@given(st.lists(st.integers(0, 100), min_size=2, max_size=18), st.integers(0, 20))
def test_uniform_height_scaling_scales_area(height, factor):
    assert Solution().maxArea([value * factor for value in height]) == factor * Solution().maxArea(
        height
    )

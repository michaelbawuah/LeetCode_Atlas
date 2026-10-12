from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0658-find-k-closest-elements").Solution


@given(st.lists(st.integers(-100, 100), min_size=1, max_size=35), st.integers(-150, 150), st.data())
def test_window_search_matches_full_distance_sort(values, target, data):
    arr = sorted(values)
    count = data.draw(st.integers(1, len(arr)))
    expected = sorted(sorted(arr, key=lambda value: (abs(value - target), value))[:count])
    assert Solution().findClosestElements(arr, count, target) == expected

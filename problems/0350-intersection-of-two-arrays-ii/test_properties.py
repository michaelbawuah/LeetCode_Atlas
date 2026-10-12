from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0350-intersection-of-two-arrays-ii").Solution


@given(
    st.lists(st.integers(0, 20), min_size=1, max_size=30),
    st.lists(st.integers(0, 20), min_size=1, max_size=30),
)
def test_multiset_intersection_matches_independent_sorted_merge(first, second):
    a, b = sorted(first), sorted(second)
    left = right = 0
    expected = []
    while left < len(a) and right < len(b):
        if a[left] == b[right]:
            expected.append(a[left])
            left += 1
            right += 1
        elif a[left] < b[right]:
            left += 1
        else:
            right += 1
    assert sorted(Solution().intersect(first, second)) == expected

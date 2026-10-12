from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0349-intersection-of-two-arrays").Solution


@given(
    st.lists(st.integers(0, 20), min_size=1, max_size=30),
    st.lists(st.integers(0, 20), min_size=1, max_size=30),
)
def test_unique_intersection_matches_membership_enumeration(first, second):
    expected = [value for value in range(21) if value in first and value in second]
    answer = Solution().intersection(first, second)
    assert sorted(answer) == expected
    assert len(answer) == len(set(answer))

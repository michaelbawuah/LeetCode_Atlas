from hypothesis import assume, given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0088-merge-sorted-array").Solution


@given(st.lists(st.integers(-100, 100), max_size=20), st.lists(st.integers(-100, 100), max_size=20))
def test_backward_merge_matches_combined_sort_and_preserves_second_input(first, second):
    assume(first or second)
    first, second = sorted(first), sorted(second)
    nums1 = first + [0] * len(second)
    original_second = second.copy()
    identity = id(nums1)
    assert Solution().merge(nums1, len(first), second, len(second)) is None
    assert nums1 == sorted(first + original_second)
    assert second == original_second and id(nums1) == identity

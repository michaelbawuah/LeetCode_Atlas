from hypothesis import assume, given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0004-median-of-two-sorted-arrays").Solution


@given(st.lists(st.integers(-100, 100), max_size=12), st.lists(st.integers(-100, 100), max_size=12))
def test_matches_combined_sort_and_is_symmetric(first, second):
    assume(first or second)
    first, second = sorted(first), sorted(second)
    merged = sorted(first + second)
    middle = len(merged) // 2
    expected = (
        float(merged[middle]) if len(merged) % 2 else (merged[middle - 1] + merged[middle]) / 2
    )
    assert Solution().findMedianSortedArrays(first, second) == expected
    assert Solution().findMedianSortedArrays(second, first) == expected


def test_partition_can_place_the_entire_shorter_array_on_one_side():
    assert Solution().findMedianSortedArrays([1, 2], [10, 11, 12, 13]) == 10.5

from itertools import combinations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0435-non-overlapping-intervals").Solution


@given(
    st.lists(
        st.tuples(st.integers(-10, 10), st.integers(1, 10)),
        min_size=1,
        max_size=9,
    )
)
def test_matches_exhaustive_compatible_subsets(raw):
    intervals = [[start, start + width] for start, width in raw]
    most_kept = 0
    for size in range(1, len(intervals) + 1):
        for chosen in combinations(intervals, size):
            ordered = sorted(chosen)
            if all(ordered[index - 1][1] <= ordered[index][0] for index in range(1, len(ordered))):
                most_kept = max(most_kept, size)
    assert Solution().eraseOverlapIntervals(intervals) == len(intervals) - most_kept


def test_shorter_interval_is_kept_even_when_it_starts_later():
    assert Solution().eraseOverlapIntervals([[1, 10], [2, 3], [3, 4]]) == 1

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0056-merge-intervals").Solution
intervals_strategy = st.lists(
    st.tuples(st.integers(0, 15), st.integers(0, 15)).map(lambda pair: sorted(pair)),
    min_size=1,
    max_size=12,
)


def coverage_oracle(intervals):
    covered = {point for start, end in intervals for point in range(2 * start, 2 * end + 1)}
    result = []
    for point in sorted(covered):
        if result and point == result[-1][1] + 1:
            result[-1][1] = point
        else:
            result.append([point, point])
    return [[start // 2, end // 2] for start, end in result]


@given(intervals_strategy)
def test_matches_integer_and_half_integer_coverage(intervals):
    assert Solution().merge(intervals) == coverage_oracle(intervals)


@given(intervals_strategy)
def test_merge_is_idempotent_and_preserves_input(intervals):
    before = [interval.copy() for interval in intervals]
    merged = Solution().merge(intervals)
    assert Solution().merge(merged) == merged
    assert intervals == before

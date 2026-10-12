from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0057-insert-interval").Solution


def coverage_oracle(intervals):
    points = sorted({point for start, end in intervals for point in range(2 * start, 2 * end + 1)})
    components = []
    for point in points:
        if components and point == components[-1][1] + 1:
            components[-1][1] = point
        else:
            components.append([point, point])
    return [[start // 2, end // 2] for start, end in components]


@given(
    st.lists(st.tuples(st.integers(0, 15), st.integers(0, 15)), max_size=10),
    st.tuples(st.integers(0, 15), st.integers(0, 15)),
)
def test_matches_coverage_union_from_independently_normalized_input(raw, new):
    intervals = coverage_oracle([sorted(pair) for pair in raw])
    new_interval = sorted(new)
    before = [interval.copy() for interval in intervals]
    expected = coverage_oracle(intervals + [new_interval])
    assert Solution().insert(intervals, new_interval) == expected
    assert intervals == before
    assert new_interval == sorted(new)


def test_touching_both_neighbors_connects_them():
    assert Solution().insert([[1, 2], [4, 5]], [2, 4]) == [[1, 5]]

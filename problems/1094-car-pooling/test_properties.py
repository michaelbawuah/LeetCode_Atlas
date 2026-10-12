from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("1094-car-pooling").Solution


@given(
    st.lists(
        st.tuples(st.integers(1, 10), st.integers(0, 14), st.integers(1, 15)),
        min_size=1,
        max_size=12,
    ),
    st.integers(1, 50),
)
def test_event_sweep_matches_direct_load_on_each_segment(raw, capacity):
    trips = [[people, start, start + width] for people, start, width in raw]
    expected = all(
        sum(people for people, start, end in trips if start <= point < end) <= capacity
        for point in range(30)
    )
    assert Solution().carPooling(trips, capacity) == expected

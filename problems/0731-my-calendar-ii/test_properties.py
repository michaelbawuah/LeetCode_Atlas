from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

MyCalendarTwo = load_module("0731-my-calendar-ii").MyCalendarTwo


@given(st.lists(st.tuples(st.integers(0, 100), st.integers(1, 30)), min_size=1, max_size=100))
def test_double_calendar_histories_match_endpoint_sweep(actions):
    obj = MyCalendarTwo()
    accepted = []
    for start, width in actions:
        end = start + width
        active = peak = 0
        proposed = accepted + [(start, end)]
        for _, delta in sorted([(a, 1) for a, b in proposed] + [(b, -1) for a, b in proposed]):
            active += delta
            peak = max(peak, active)
        expected = peak <= 2
        assert obj.book(start, end) == expected
        if expected:
            accepted.append((start, end))

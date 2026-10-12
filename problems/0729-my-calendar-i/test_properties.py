from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

MyCalendar = load_module("0729-my-calendar-i").MyCalendar


@given(st.lists(st.tuples(st.integers(0, 100), st.integers(1, 30)), min_size=1, max_size=100))
def test_calendar_histories_match_endpoint_sweep(actions):
    obj = MyCalendar()
    accepted = []
    for start, width in actions:
        end = start + width
        active = peak = 0
        for _, delta in sorted(
            [(a, 1) for a, b in accepted + [(start, end)]]
            + [(b, -1) for a, b in accepted + [(start, end)]]
        ):
            active += delta
            peak = max(peak, active)
        expected = peak <= 1
        assert obj.book(start, end) == expected
        if expected:
            accepted.append((start, end))

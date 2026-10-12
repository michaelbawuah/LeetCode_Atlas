from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

RecentCounter = load_module("0933-number-of-recent-calls").RecentCounter


@given(st.lists(st.integers(1, 5000), min_size=1, max_size=100))
def test_recent_counts_match_full_timestamp_history(increments):
    obj = RecentCounter()
    history = []
    time = 0
    for increment in increments:
        time += increment
        history.append(time)
        assert obj.ping(time) == sum(time - 3000 <= old <= time for old in history)

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0739-daily-temperatures").Solution


@given(st.lists(st.integers(30, 100), min_size=1, max_size=40))
def test_waits_match_first_warmer_day(temperatures):
    expected = [
        next((j - i for j in range(i + 1, len(temperatures)) if temperatures[j] > value), 0)
        for i, value in enumerate(temperatures)
    ]
    snapshot = list(temperatures)
    assert Solution().dailyTemperatures(temperatures) == expected
    assert temperatures == snapshot

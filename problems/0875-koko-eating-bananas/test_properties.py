from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0875-koko-eating-bananas").Solution


@given(piles=st.lists(st.integers(1, 45), min_size=1, max_size=15), data=st.data())
def test_speed_matches_exhaustive_candidates(piles, data):
    hours = data.draw(st.integers(len(piles), sum(piles) + 10))

    def feasible(speed):
        # Count consumed chunks explicitly, independent of the ceiling formula.
        return sum(len(range(0, pile, speed)) for pile in piles) <= hours

    expected = next(speed for speed in range(1, max(piles) + 1) if feasible(speed))
    snapshot = list(piles)
    assert Solution().minEatingSpeed(piles, hours) == expected
    assert piles == snapshot

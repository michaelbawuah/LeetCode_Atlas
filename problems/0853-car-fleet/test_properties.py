from fractions import Fraction

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0853-car-fleet").Solution


@given(
    positions=st.lists(st.integers(0, 100), min_size=1, max_size=25, unique=True), data=st.data()
)
def test_fleets_match_all_cars_ahead_comparison(positions, data):
    speeds = data.draw(
        st.lists(st.integers(1, 30), min_size=len(positions), max_size=len(positions))
    )
    target = 101
    cars = sorted(zip(positions, speeds, strict=True))
    arrivals = [Fraction(target - start, speed) for start, speed in cars]
    # A distinct fleet is a strict suffix maximum in the original arrival times.
    expected = sum(
        all(arrival > ahead for ahead in arrivals[index + 1 :])
        for index, arrival in enumerate(arrivals)
    )
    position_snapshot, speed_snapshot = list(positions), list(speeds)
    assert Solution().carFleet(target, positions, speeds) == expected
    assert positions == position_snapshot
    assert speeds == speed_snapshot

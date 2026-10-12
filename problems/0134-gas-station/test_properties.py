from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0134-gas-station"


@st.composite
def circuits(draw):
    count = draw(st.integers(1, 18))
    gas = draw(st.lists(st.integers(0, 20), min_size=count, max_size=count))
    cost = draw(st.lists(st.integers(0, 20), min_size=count, max_size=count))
    return gas, cost


def valid_starts(gas, cost):
    starts = []
    for start in range(len(gas)):
        fuel = 0
        for step in range(len(gas)):
            index = (start + step) % len(gas)
            fuel += gas[index] - cost[index]
            if fuel < 0:
                break
        else:
            starts.append(start)
    return starts


@given(circuits())
def test_candidate_reset_returns_an_independently_simulated_valid_start(case):
    gas, cost = case
    witnesses = valid_starts(gas, cost)
    actual = evaluate(FOLDER, args=[gas, cost])
    assert type(actual) is int
    assert actual in witnesses if witnesses else actual == -1

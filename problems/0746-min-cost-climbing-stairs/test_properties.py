from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0746-min-cost-climbing-stairs"


def enumerate_paid_routes(cost, position):
    if position >= len(cost):
        return 0
    return cost[position] + min(
        enumerate_paid_routes(cost, position + 1),
        enumerate_paid_routes(cost, position + 2),
    )


@settings(max_examples=80)
@given(st.lists(st.integers(0, 999), min_size=2, max_size=11))
def test_rolling_cost_matches_complete_route_search(cost):
    expected = min(enumerate_paid_routes(cost, 0), enumerate_paid_routes(cost, 1))
    assert evaluate(FOLDER, args=[cost]) == expected

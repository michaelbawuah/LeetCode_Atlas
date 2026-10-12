from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0322-coin-change"


def shortest_coin_path(coins, amount):
    frontier = {0}
    visited = {0}
    distance = 0
    while frontier:
        if amount in frontier:
            return distance
        next_frontier = {
            total + coin
            for total in frontier
            for coin in coins
            if total + coin <= amount and total + coin not in visited
        }
        visited.update(next_frontier)
        frontier = next_frontier
        distance += 1
    return -1


@settings(max_examples=100)
@given(
    st.lists(st.integers(1, 12), min_size=1, max_size=5, unique=True),
    st.integers(0, 40),
)
def test_amount_dp_matches_breadth_first_coin_search(coins, amount):
    assert evaluate(FOLDER, args=[coins, amount]) == shortest_coin_path(coins, amount)

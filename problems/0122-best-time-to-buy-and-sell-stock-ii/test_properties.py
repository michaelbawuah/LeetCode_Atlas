from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0122-best-time-to-buy-and-sell-stock-ii").Solution


@given(st.lists(st.integers(0, 20), min_size=1, max_size=9))
def test_greedy_gain_matches_enumeration_of_legal_trading_states(prices):
    states = {(False, 0)}
    for price in prices:
        next_states = set(states)
        for holding, balance in states:
            next_states.add((False, balance + price) if holding else (True, balance - price))
        states = next_states
    expected = max(balance for holding, balance in states if not holding)
    assert Solution().maxProfit(prices) == expected

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0121-best-time-to-buy-and-sell-stock").Solution


@given(st.lists(st.integers(0, 10000), min_size=1, max_size=30))
def test_profit_matches_all_legal_trades(prices):
    expected = max(
        [0] + [prices[j] - prices[i] for i in range(len(prices)) for j in range(i + 1, len(prices))]
    )
    snapshot = list(prices)
    assert Solution().maxProfit(prices) == expected
    assert prices == snapshot

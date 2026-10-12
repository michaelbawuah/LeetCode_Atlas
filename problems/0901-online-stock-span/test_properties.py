from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

StockSpanner = load_module("0901-online-stock-span").StockSpanner


@given(st.lists(st.integers(1, 100000), min_size=1, max_size=100))
def test_all_spans_match_backward_prefix_scan(prices):
    obj = StockSpanner()
    history = []
    for price in prices:
        history.append(price)
        expected = 0
        for old in reversed(history):
            if old > price:
                break
            expected += 1
        assert obj.next(price) == expected

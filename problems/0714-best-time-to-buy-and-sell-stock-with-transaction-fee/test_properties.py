from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0714-best-time-to-buy-and-sell-stock-with-transaction-fee"


def exhaustive_profit(prices, limit, fee=0):
    def visit(day, holding, remaining):
        if day == len(prices):
            return -(10**12) if holding else 0
        best = visit(day + 1, holding, remaining)
        if holding and remaining:
            best = max(best, prices[day] - fee + visit(day + 1, False, remaining - 1))
        elif not holding and remaining:
            best = max(best, -prices[day] + visit(day + 1, True, remaining))
        return best

    return visit(0, False, limit)


def oracle(prices, fee):
    return exhaustive_profit(prices, len(prices), fee)


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.lists(st.integers(1, 20), min_size=1, max_size=8), st.integers(0, 10)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

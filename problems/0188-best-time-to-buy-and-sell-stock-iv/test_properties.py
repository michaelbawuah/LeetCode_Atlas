from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0188-best-time-to-buy-and-sell-stock-iv"


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


def oracle(k, prices):
    return exhaustive_profit(prices, k)


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.integers(1, 5), st.lists(st.integers(0, 20), min_size=1, max_size=8)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

from itertools import product

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0518-coin-change-ii"


@settings(max_examples=80)
@given(
    st.integers(0, 16),
    st.lists(st.integers(1, 9), min_size=1, max_size=4, unique=True),
)
def test_coin_order_dp_matches_complete_multiplicity_vectors(amount, coins):
    expected = sum(
        sum(coin * count for coin, count in zip(coins, counts, strict=True)) == amount
        for counts in product(*(range(amount // coin + 1) for coin in coins))
    )
    assert evaluate(FOLDER, args=[amount, coins]) == expected


def test_unreachable_odd_amount_keeps_final_count_small_despite_huge_other_states():
    assert evaluate(FOLDER, args=[4999, list(range(2, 601, 2))]) == 0

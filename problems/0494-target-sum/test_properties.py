from itertools import product

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0494-target-sum"


@settings(max_examples=80)
@given(st.lists(st.integers(0, 8), min_size=1, max_size=12), st.integers(-40, 40))
def test_frequency_dp_matches_every_sign_assignment(values, target):
    expected = sum(
        sum(sign * value for sign, value in zip(signs, values, strict=True)) == target
        for signs in product((-1, 1), repeat=len(values))
    )
    assert evaluate(FOLDER, args=[values, target]) == expected

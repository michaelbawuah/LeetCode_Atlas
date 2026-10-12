from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0338-counting-bits"


@settings(max_examples=80)
@given(st.integers(0, 400))
def test_prefix_dp_matches_independent_binary_digit_counts(n):
    expected = [format(value, "b").count("1") for value in range(n + 1)]
    assert evaluate(FOLDER, args=[n]) == expected

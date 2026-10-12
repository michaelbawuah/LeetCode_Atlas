from math import comb

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0096-unique-binary-search-trees"


def oracle(n):
    return comb(2 * n, n) // (n + 1)


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.integers(1, 19)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

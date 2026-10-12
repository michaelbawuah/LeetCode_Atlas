from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0377-combination-sum-iv"


def oracle(values, target):
    if target == 0:
        return 1
    if target < 0:
        return 0
    return sum(oracle(values, target - value) for value in values)


@settings(max_examples=60, deadline=None)
@given(
    st.tuples(st.lists(st.integers(1, 8), min_size=1, max_size=4, unique=True), st.integers(1, 10))
)
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

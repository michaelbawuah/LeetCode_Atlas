from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0740-delete-and-earn"


def oracle(values):
    choices = sorted(set(values))
    best = 0
    for mask in range(1 << len(choices)):
        selected = {value for index, value in enumerate(choices) if mask & (1 << index)}
        if not any(value + 1 in selected for value in selected):
            best = max(best, sum(value for value in values if value in selected))
    return best


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.lists(st.integers(1, 9), min_size=1, max_size=14)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

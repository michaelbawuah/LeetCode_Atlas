from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0312-burst-balloons"


def oracle(values):
    if not values:
        return 0
    return max(
        (values[index - 1] if index else 1)
        * value
        * (values[index + 1] if index + 1 < len(values) else 1)
        + oracle(values[:index] + values[index + 1 :])
        for index, value in enumerate(values)
    )


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.lists(st.integers(0, 8), min_size=1, max_size=6)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

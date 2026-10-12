from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0198-house-robber"


def exhaustive_best(values):
    answer = 0
    for mask in range(1 << len(values)):
        if mask & (mask << 1):
            continue
        total = sum(value for index, value in enumerate(values) if mask & (1 << index))
        answer = max(answer, total)
    return answer


@settings(max_examples=80)
@given(st.lists(st.integers(0, 400), min_size=1, max_size=14))
def test_rolling_dp_matches_exhaustive_subsets(values):
    assert evaluate(FOLDER, args=[values]) == exhaustive_best(values)

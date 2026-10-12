from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0213-house-robber-ii"


def enumerate_circular_subsets(values):
    answer = 0
    for mask in range(1 << len(values)):
        if mask & (mask << 1):
            continue
        if len(values) > 1 and mask & 1 and mask & (1 << (len(values) - 1)):
            continue
        answer = max(
            answer,
            sum(value for index, value in enumerate(values) if mask & (1 << index)),
        )
    return answer


@settings(max_examples=80)
@given(st.lists(st.integers(0, 1000), min_size=1, max_size=12))
def test_endpoint_split_matches_exhaustive_circular_subsets(values):
    assert evaluate(FOLDER, args=[values]) == enumerate_circular_subsets(values)

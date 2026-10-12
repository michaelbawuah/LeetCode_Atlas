from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0300-longest-increasing-subsequence"


def enumerate_increasing_subsequences(values):
    answer = 0
    for mask in range(1 << len(values)):
        selected = [value for index, value in enumerate(values) if mask & (1 << index)]
        if all(first < second for first, second in zip(selected, selected[1:], strict=False)):
            answer = max(answer, len(selected))
    return answer


@settings(max_examples=80)
@given(st.lists(st.integers(-20, 20), min_size=1, max_size=12))
def test_binary_search_tails_matches_subsequence_enumeration(values):
    assert evaluate(FOLDER, args=[values]) == enumerate_increasing_subsequences(values)

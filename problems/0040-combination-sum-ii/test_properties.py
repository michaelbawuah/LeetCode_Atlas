from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0040-combination-sum-ii"


@settings(max_examples=80)
@given(st.lists(st.integers(1, 8), min_size=1, max_size=10), st.integers(1, 30))
def test_single_use_search_matches_all_position_subsets(values, target):
    expected = set()
    for mask in range(1 << len(values)):
        parts = [value for index, value in enumerate(values) if mask & (1 << index)]
        if sum(parts) == target:
            expected.add(tuple(sorted(parts)))
    answer = evaluate(FOLDER, args=[values, target])
    assert len(answer) == len(expected)
    assert {tuple(sorted(parts)) for parts in answer} == expected

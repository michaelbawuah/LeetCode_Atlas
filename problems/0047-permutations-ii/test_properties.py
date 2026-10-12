from itertools import permutations

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0047-permutations-ii"


@settings(max_examples=70)
@given(st.lists(st.integers(-2, 2), min_size=1, max_size=7))
def test_frequency_search_matches_position_permutations_with_deduplication(values):
    expected = set(permutations(values))
    answer = evaluate(FOLDER, args=[values])
    assert len(answer) == len(expected)
    assert {tuple(parts) for parts in answer} == expected

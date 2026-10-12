from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0416-partition-equal-subset-sum"


@settings(max_examples=80)
@given(st.lists(st.integers(1, 12), min_size=1, max_size=14))
def test_descending_subset_dp_matches_all_index_subsets(values):
    total = sum(values)
    expected = total % 2 == 0 and any(
        sum(value for index, value in enumerate(values) if mask & (1 << index)) * 2 == total
        for mask in range(1 << len(values))
    )
    assert evaluate(FOLDER, args=[values]) == expected

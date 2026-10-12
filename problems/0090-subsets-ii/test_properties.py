from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import load_module

FOLDER = "0090-subsets-ii"


@settings(max_examples=80)
@given(st.lists(st.integers(-3, 3), min_size=1, max_size=9))
def test_skip_siblings_matches_canonical_index_subsets(values):
    expected = {
        tuple(sorted(value for index, value in enumerate(values) if mask & (1 << index)))
        for mask in range(1 << len(values))
    }
    before = values.copy()
    answer = load_module(FOLDER).Solution().subsetsWithDup(values)
    assert len(answer) == len(expected)
    assert {tuple(sorted(parts)) for parts in answer} == expected
    assert values == before

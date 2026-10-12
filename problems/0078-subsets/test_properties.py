from itertools import combinations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0078-subsets"


@given(st.lists(st.integers(-10, 10), min_size=1, max_size=8, unique=True))
def test_iterative_expansion_matches_every_subset_size(nums):
    expected = {
        tuple(sorted(subset))
        for size in range(len(nums) + 1)
        for subset in combinations(nums, size)
    }
    actual = evaluate(FOLDER, args=[nums])
    assert len(actual) == 2 ** len(nums)
    assert {tuple(sorted(subset)) for subset in actual} == expected

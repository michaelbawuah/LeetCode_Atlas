from itertools import combinations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0015-3sum").Solution


def canonical(rows):
    return sorted(tuple(row) for row in rows)


@given(st.lists(st.integers(-6, 6), min_size=3, max_size=12))
def test_matches_exhaustive_distinct_index_triples(nums):
    expected = {tuple(sorted(triple)) for triple in combinations(nums, 3) if sum(triple) == 0}
    answer = Solution().threeSum(nums)
    actual = {tuple(sorted(triple)) for triple in answer}
    assert actual == expected
    assert len(answer) == len(actual)


@given(st.lists(st.integers(-6, 6), min_size=3, max_size=12))
def test_input_order_does_not_change_unique_triples(nums):
    assert canonical(Solution().threeSum(nums)) == canonical(Solution().threeSum(nums[::-1]))

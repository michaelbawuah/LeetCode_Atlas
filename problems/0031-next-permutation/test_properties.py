from itertools import permutations

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0031-next-permutation").Solution


@given(st.lists(st.integers(0, 4), min_size=1, max_size=6))
def test_matches_enumerated_distinct_lexicographic_permutations(nums):
    original = tuple(nums)
    ordered = sorted(set(permutations(original)))
    expected = ordered[(ordered.index(original) + 1) % len(ordered)]
    identity = id(nums)
    assert Solution().nextPermutation(nums) is None
    assert tuple(nums) == expected
    assert id(nums) == identity

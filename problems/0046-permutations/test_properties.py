from itertools import permutations
from math import factorial

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0046-permutations"


@given(st.lists(st.integers(-10, 10), min_size=1, max_size=6, unique=True))
def test_all_orderings_match_exhaustive_permutation_iterator(nums):
    actual = evaluate(FOLDER, args=[nums])
    assert len(actual) == factorial(len(nums))
    assert {tuple(answer) for answer in actual} == set(permutations(nums))
    assert all(len(answer) == len(nums) for answer in actual)

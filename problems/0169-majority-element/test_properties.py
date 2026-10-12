from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0169-majority-element").Solution


@given(st.integers(-20, 20), st.lists(st.integers(-20, 20), max_size=8), st.data())
def test_guaranteed_majority_matches_sorting_median(majority, noise, data):
    nums = [majority] * (len(noise) + 1) + noise
    shuffled = list(data.draw(st.permutations(nums)))
    expected = sorted(shuffled)[len(shuffled) // 2]
    assert expected == majority
    assert Solution().majorityElement(shuffled) == expected


@given(st.integers(-100, 100), st.integers(1, 30))
def test_all_equal_values_are_the_majority(value, size):
    assert Solution().majorityElement([value] * size) == value

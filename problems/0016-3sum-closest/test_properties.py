from itertools import combinations

from hypothesis import assume, given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0016-3sum-closest").Solution


@given(st.lists(st.integers(-10, 10), min_size=3, max_size=9), st.integers(-30, 30))
def test_matches_enumerated_sums_with_a_unique_closest_value(nums, target):
    sums = {sum(triple) for triple in combinations(nums, 3)}
    distance = min(abs(total - target) for total in sums)
    closest = [total for total in sums if abs(total - target) == distance]
    assume(len(closest) == 1)
    original = nums.copy()
    assert Solution().threeSumClosest(nums, target) == closest[0]
    assert Solution().threeSumClosest(nums[::-1], target) == closest[0]
    assert nums == original


def test_large_target_can_choose_the_largest_available_sum():
    assert Solution().threeSumClosest([-5, -2, 1, 4], 100) == 3

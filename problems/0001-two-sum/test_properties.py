from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0001-two-sum").Solution


@given(st.lists(st.integers(-20, 20), min_size=2, max_size=12), st.data())
def test_returned_pair_is_a_brute_force_witness(nums, data):
    first = data.draw(st.integers(0, len(nums) - 1))
    second = data.draw(st.sampled_from([i for i in range(len(nums)) if i != first]))
    target = nums[first] + nums[second]
    witnesses = {
        (i, j)
        for i in range(len(nums))
        for j in range(i + 1, len(nums))
        if nums[i] + nums[j] == target
    }
    answer = Solution().twoSum(nums, target)
    assert len(answer) == 2
    assert tuple(sorted(answer)) in witnesses


def test_does_not_reuse_an_index_before_seeing_its_partner():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]

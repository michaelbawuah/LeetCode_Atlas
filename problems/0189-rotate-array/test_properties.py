from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0189-rotate-array").Solution


@given(st.lists(st.integers(-100, 100), min_size=1, max_size=30), st.integers(0, 100000))
def test_in_place_rotation_matches_modular_index_mapping(nums, k):
    original = nums.copy()
    identity = id(nums)
    expected = [original[(index - k) % len(original)] for index in range(len(original))]
    assert Solution().rotate(nums, k) is None
    assert nums == expected
    assert id(nums) == identity
    assert len(nums) == len(original)


@given(
    st.lists(st.integers(-100, 100), min_size=1, max_size=30),
    st.integers(0, 10000),
    st.integers(0, 10000),
)
def test_composed_rotations_add_their_steps(nums, first, second):
    once = nums.copy()
    Solution().rotate(nums, first)
    Solution().rotate(nums, second)
    Solution().rotate(once, first + second)
    assert nums == once

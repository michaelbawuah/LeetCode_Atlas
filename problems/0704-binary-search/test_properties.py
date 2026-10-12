from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0704-binary-search").Solution


@given(
    st.lists(st.integers(-10000, 10000), min_size=1, max_size=40, unique=True),
    st.integers(-10000, 10000),
)
def test_search_matches_linear_lookup(values, target):
    nums = sorted(values)
    snapshot = list(nums)
    expected = nums.index(target) if target in nums else -1
    assert Solution().search(nums, target) == expected
    assert nums == snapshot


@given(st.lists(st.integers(-10000, 10000), min_size=1, max_size=40, unique=True))
def test_every_present_value_is_found(values):
    nums = sorted(values)
    for index, target in enumerate(nums):
        assert Solution().search(nums, target) == index

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0033-search-in-rotated-sorted-array").Solution


@given(
    values=st.lists(st.integers(-10000, 10000), min_size=1, max_size=35, unique=True),
    target=st.integers(-10000, 10000),
    data=st.data(),
)
def test_rotated_search_matches_linear_lookup(values, target, data):
    ordered = sorted(values)
    pivot = data.draw(st.integers(0, len(ordered) - 1), label="rotation pivot")
    nums = ordered[pivot:] + ordered[:pivot]
    snapshot = list(nums)
    expected = nums.index(target) if target in nums else -1
    assert Solution().search(nums, target) == expected
    assert nums == snapshot


@given(
    values=st.lists(st.integers(-10000, 10000), min_size=1, max_size=20, unique=True),
    data=st.data(),
)
def test_every_value_is_found_after_rotation(values, data):
    ordered = sorted(values)
    pivot = data.draw(st.integers(0, len(ordered) - 1), label="rotation pivot")
    nums = ordered[pivot:] + ordered[:pivot]
    for index, target in enumerate(nums):
        assert Solution().search(nums, target) == index

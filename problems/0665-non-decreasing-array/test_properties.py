from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0665-non-decreasing-array").Solution


@given(st.lists(st.integers(-5, 5), min_size=1, max_size=10))
def test_virtual_repair_matches_all_single_value_replacements(nums):
    candidates = [nums]
    for index in range(len(nums)):
        for value in range(-6, 7):
            replaced = nums.copy()
            replaced[index] = value
            candidates.append(replaced)
    expected = any(
        all(a <= b for a, b in zip(values, values[1:], strict=False)) for values in candidates
    )
    original = nums.copy()
    assert Solution().checkPossibility(nums) == expected
    assert nums == original

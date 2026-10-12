from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0448-find-all-numbers-disappeared-in-an-array").Solution


@given(st.integers(1, 30), st.data())
def test_sign_marking_matches_set_difference_and_preserves_absolute_values(size, data):
    nums = data.draw(st.lists(st.integers(1, size), min_size=size, max_size=size))
    original = nums.copy()
    expected = sorted(set(range(1, size + 1)) - set(original))
    actual = Solution().findDisappearedNumbers(nums)
    assert sorted(actual) == expected
    assert len(actual) == len(set(actual))
    assert [abs(value) for value in nums] == original


def test_repeated_marks_do_not_toggle_a_number_back_to_positive():
    assert Solution().findDisappearedNumbers([1, 1]) == [2]

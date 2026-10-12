from collections import Counter

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0287-find-the-duplicate-number").Solution


@given(st.integers(1, 25), st.data())
def test_cycle_entry_matches_counting_with_arbitrary_duplicate_multiplicity(n, data):
    duplicate = data.draw(st.integers(1, n))
    copies = data.draw(st.integers(2, n + 1))
    available = [value for value in range(1, n + 1) if value != duplicate]
    others = (
        data.draw(
            st.lists(
                st.sampled_from(available),
                min_size=n + 1 - copies,
                max_size=n + 1 - copies,
                unique=True,
            )
        )
        if available
        else []
    )
    nums = [duplicate] * copies + others
    nums = list(data.draw(st.permutations(nums)))
    original = nums.copy()
    expected = next(value for value, count in Counter(nums).items() if count > 1)
    assert Solution().findDuplicate(nums) == expected
    assert nums == original

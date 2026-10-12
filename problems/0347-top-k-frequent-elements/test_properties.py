from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0347-top-k-frequent-elements").Solution


@given(st.lists(st.integers(1, 10), min_size=1, max_size=7, unique=True), st.data())
def test_matches_full_sort_for_distinct_frequencies(frequencies, data):
    values = data.draw(
        st.lists(
            st.integers(-20, 20),
            min_size=len(frequencies),
            max_size=len(frequencies),
            unique=True,
        )
    )
    nums = [value for value, count in zip(values, frequencies, strict=True) for _ in range(count)]
    k = data.draw(st.integers(1, len(values)))
    expected = sorted(values, key=nums.count, reverse=True)[:k]
    answer = Solution().topKFrequent(nums, k)
    assert len(answer) == k
    assert set(answer) == set(expected)


def test_tied_frequencies_are_valid_when_entire_tie_is_selected():
    answer = Solution().topKFrequent([4, 4, 5, 5, 6], 2)
    assert len(answer) == 2
    assert set(answer) == {4, 5}

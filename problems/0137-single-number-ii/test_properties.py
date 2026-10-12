from collections import Counter

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0137-single-number-ii").Solution


@given(
    st.lists(st.integers(-2147483648, 2147483647), min_size=1, max_size=7, unique=True), st.data()
)
def test_bit_states_match_occurrence_counter_for_signed_values(values, data):
    single = data.draw(st.sampled_from(values))
    nums = [single] + [value for value in values if value != single for _ in range(3)]
    nums = list(data.draw(st.permutations(nums)))
    expected = next(value for value, count in Counter(nums).items() if count == 1)
    assert Solution().singleNumber(nums) == expected

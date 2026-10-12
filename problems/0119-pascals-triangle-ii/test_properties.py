from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0119-pascals-triangle-ii").Solution


@given(st.integers(0, 33))
def test_coefficient_ratio_matches_independent_pascal_expansion(index):
    expected = [1]
    for _ in range(index):
        expected = [1] + [expected[i - 1] + expected[i] for i in range(1, len(expected))] + [1]
    actual = Solution().getRow(index)
    assert actual == expected
    assert actual == actual[::-1] and sum(actual) == 2**index

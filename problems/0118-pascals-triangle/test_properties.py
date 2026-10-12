from math import comb

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0118-pascals-triangle").Solution


@given(st.integers(1, 30))
def test_rows_match_independent_binomial_coefficients(count):
    rows = Solution().generate(count)
    assert rows == [[comb(row, column) for column in range(row + 1)] for row in range(count)]
    assert len({id(row) for row in rows}) == count
    assert [sum(row) for row in rows] == [2**index for index in range(count)]

import math
from fractions import Fraction

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0050-powx-n").Solution


@given(x=st.integers(-5, 5).filter(lambda value: value != 0), n=st.integers(-5, 5))
def test_binary_power_matches_exact_rational_power(x, n):
    expected = float(Fraction(x) ** n)
    assert math.isclose(Solution().myPow(float(x), n), expected, rel_tol=1e-9, abs_tol=1e-12)

from functools import reduce
from operator import and_

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0201-bitwise-and-of-numbers-range"


@settings(max_examples=100)
@given(st.integers(0, 500), st.data())
def test_common_prefix_matches_direct_range_reduction(left, data):
    right = data.draw(st.integers(left, min(530, left + 30)))
    expected = reduce(and_, range(left, right + 1))
    assert evaluate(FOLDER, args=[left, right]) == expected

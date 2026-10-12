from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0344-reverse-string").Solution


@given(st.lists(st.sampled_from(list("abcXYZ!? ")), min_size=1, max_size=100))
def test_in_place_reversal_matches_slicing(values):
    snapshot = list(values)
    identity = id(values)
    assert Solution().reverseString(values) is None
    assert values == snapshot[::-1]
    assert id(values) == identity

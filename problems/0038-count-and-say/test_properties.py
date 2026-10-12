from itertools import groupby

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0038-count-and-say").Solution


@given(st.integers(1, 15))
def test_terms_match_groupby_run_encoding(n):
    expected = "1"
    for _ in range(n - 1):
        expected = "".join(str(len(list(group))) + letter for letter, group in groupby(expected))
    assert Solution().countAndSay(n) == expected

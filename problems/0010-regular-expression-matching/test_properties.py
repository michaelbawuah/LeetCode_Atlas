import re

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0010-regular-expression-matching").Solution


@given(
    s=st.text(alphabet="ab", min_size=1, max_size=8),
    tokens=st.lists(
        st.tuples(st.sampled_from(["a", "b", "."]), st.booleans()), min_size=1, max_size=6
    ),
)
def test_match_agrees_with_standard_regex_fullmatch(s, tokens):
    pattern = "".join(atom + ("*" if repeat else "") for atom, repeat in tokens)
    assert Solution().isMatch(s, pattern) == (re.fullmatch(pattern, s) is not None)

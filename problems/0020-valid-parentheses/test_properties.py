from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0020-valid-parentheses").Solution


@given(st.text(alphabet="()[]{}", min_size=1, max_size=36))
def test_validity_matches_pair_cancellation(s):
    reduced = s
    while True:
        next_reduced = reduced.replace("()", "").replace("[]", "").replace("{}", "")
        if next_reduced == reduced:
            break
        reduced = next_reduced
    assert Solution().isValid(s) == (reduced == "")

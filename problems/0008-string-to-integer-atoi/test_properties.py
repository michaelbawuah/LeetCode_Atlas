import re

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0008-string-to-integer-atoi").Solution


@given(st.text(alphabet=" 0123456789+-abc.", max_size=80))
def test_parser_matches_anchored_digit_prefix(s):
    match = re.match(r"^ *([+-]?[0-9]+)", s)
    expected = int(match.group(1)) if match else 0
    expected = max(-(2**31), min(2**31 - 1, expected))
    assert Solution().myAtoi(s) == expected

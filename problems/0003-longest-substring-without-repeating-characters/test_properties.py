from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0003-longest-substring-without-repeating-characters").Solution


@given(st.text(alphabet="abCD01 !?", max_size=24))
def test_longest_matches_substring_enumeration(s):
    expected = max(
        [0]
        + [
            j - i
            for i in range(len(s))
            for j in range(i + 1, len(s) + 1)
            if len(set(s[i:j])) == j - i
        ]
    )
    assert Solution().lengthOfLongestSubstring(s) == expected

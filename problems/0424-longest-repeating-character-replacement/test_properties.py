from collections import Counter

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0424-longest-repeating-character-replacement").Solution


@given(s=st.text(alphabet="ABCDE", min_size=1, max_size=22), data=st.data())
def test_replacement_matches_every_window(s, data):
    k = data.draw(st.integers(0, len(s)), label="replacement budget")
    expected = 0
    for start in range(len(s)):
        for stop in range(start + 1, len(s) + 1):
            window = s[start:stop]
            replacements = len(window) - max(Counter(window).values())
            if replacements <= k:
                expected = max(expected, len(window))
    assert Solution().characterReplacement(s, k) == expected

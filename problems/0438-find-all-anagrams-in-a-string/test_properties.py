from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0438-find-all-anagrams-in-a-string").Solution


@given(
    s=st.text(alphabet="abcd", min_size=1, max_size=40),
    p=st.text(alphabet="abcd", min_size=1, max_size=10),
)
def test_windows_match_sorted_substrings(s, p):
    expected = [i for i in range(len(s) - len(p) + 1) if sorted(s[i : i + len(p)]) == sorted(p)]
    assert Solution().findAnagrams(s, p) == expected

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0028-find-the-index-of-the-first-occurrence-in-a-string").Solution


@given(
    haystack=st.text(alphabet="abc", min_size=1, max_size=80),
    needle=st.text(alphabet="abc", min_size=1, max_size=25),
)
def test_kmp_matches_standard_find(haystack, needle):
    assert Solution().strStr(haystack, needle) == haystack.find(needle)

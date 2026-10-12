from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0567-permutation-in-string").Solution


@given(
    st.text(alphabet="abcd", min_size=1, max_size=9),
    st.text(alphabet="abcd", min_size=1, max_size=22),
)
def test_inclusion_matches_sorted_windows(s1, s2):
    width = len(s1)
    expected = any(
        sorted(s2[start : start + width]) == sorted(s1) for start in range(len(s2) - width + 1)
    )
    assert Solution().checkInclusion(s1, s2) == expected

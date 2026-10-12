from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0076-minimum-window-substring").Solution


def covers(window, target):
    return all(window.count(character) >= target.count(character) for character in set(target))


@given(
    st.text(alphabet="abABc", min_size=1, max_size=12),
    st.text(alphabet="abABc", min_size=1, max_size=5),
)
def test_matches_exhaustive_minimum_length(s, t):
    candidates = [
        s[left:right]
        for left in range(len(s))
        for right in range(left + 1, len(s) + 1)
        if covers(s[left:right], t)
    ]
    answer = Solution().minWindow(s, t)
    if not candidates:
        assert answer == ""
    else:
        assert answer in s
        assert covers(answer, t)
        assert len(answer) == min(map(len, candidates))


def test_counts_repeated_requirements_rather_than_distinct_letters():
    assert Solution().minWindow("acbbaca", "aba") == "baca"

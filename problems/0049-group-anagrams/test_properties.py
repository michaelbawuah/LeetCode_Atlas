from collections import Counter

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0049-group-anagrams").Solution


def canonical(groups):
    return sorted(tuple(sorted(group)) for group in groups)


@given(st.lists(st.text(alphabet="abcxyz", max_size=8), min_size=1, max_size=20))
def test_matches_sorted_character_groups_and_preserves_multiplicity(words):
    expected: dict[str, list[str]] = {}
    for word in words:
        expected.setdefault("".join(sorted(word)), []).append(word)
    actual = Solution().groupAnagrams(words)
    assert canonical(actual) == canonical(expected.values())
    assert Counter(word for group in actual for word in group) == Counter(words)

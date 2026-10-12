from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0017-letter-combinations-of-a-phone-number").Solution


@given(st.text(alphabet="23456789", max_size=4))
def test_combinations_match_iterative_expansion(digits):
    mapping = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    expected = [""] if digits else []
    for digit in digits:
        expected = [prefix + letter for prefix in expected for letter in mapping[int(digit) - 2]]
    actual = Solution().letterCombinations(digits)
    assert len(actual) == len(set(actual))
    assert sorted(actual) == sorted(expected)

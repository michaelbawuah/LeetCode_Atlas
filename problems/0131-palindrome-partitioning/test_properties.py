from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0131-palindrome-partitioning"


def palindromic_cut_masks(text):
    answers = set()
    for mask in range(1 << (len(text) - 1)):
        parts, start = [], 0
        for end in range(1, len(text)):
            if mask & (1 << (end - 1)):
                parts.append(text[start:end])
                start = end
        parts.append(text[start:])
        if all(part == part[::-1] for part in parts):
            answers.add(tuple(parts))
    return answers


@settings(max_examples=80)
@given(st.text(alphabet="abc", min_size=1, max_size=9))
def test_precomputed_palindromes_match_all_cut_positions(text):
    expected = palindromic_cut_masks(text)
    answer = evaluate(FOLDER, args=[text])
    assert len(answer) == len(expected)
    assert {tuple(parts) for parts in answer} == expected

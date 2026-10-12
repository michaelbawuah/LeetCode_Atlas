from itertools import product
from math import comb

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0022-generate-parentheses"


def balanced_strings(count):
    answers = []
    for characters in product("()", repeat=2 * count):
        balance = 0
        for character in characters:
            balance += 1 if character == "(" else -1
            if balance < 0:
                break
        else:
            if balance == 0:
                answers.append("".join(characters))
    return answers


@given(st.integers(1, 6))
def test_pruned_prefixes_match_all_binary_strings_with_legal_balances(count):
    actual = evaluate(FOLDER, args=[count])
    expected = balanced_strings(count)
    assert len(actual) == len(expected)
    assert set(actual) == set(expected)


def test_largest_official_size_has_the_catalan_count():
    count = 8
    actual = evaluate(FOLDER, args=[count])
    assert len(actual) == comb(2 * count, count) // (count + 1)
    assert len(set(actual)) == len(actual)
    assert all(len(answer) == 2 * count for answer in actual)

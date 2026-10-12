from itertools import product

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0678-valid-parenthesis-string"


def any_expansion_balanced(s):
    for replacements in product(("", "(", ")"), repeat=s.count("*")):
        replacement = iter(replacements)
        expanded = "".join(next(replacement) if character == "*" else character for character in s)
        balance = 0
        for character in expanded:
            balance += 1 if character == "(" else -1
            if balance < 0:
                break
        else:
            if balance == 0:
                return True
    return False


@given(st.text(alphabet="()*", min_size=1, max_size=8))
def test_balance_interval_matches_all_wildcard_replacements(s):
    assert evaluate(FOLDER, args=[s]) is any_expansion_balanced(s)

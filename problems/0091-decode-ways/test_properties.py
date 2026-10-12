from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0091-decode-ways"


def enumerate_valid_groupings(text, offset=0):
    if offset == len(text):
        return 1
    if text[offset] == "0":
        return 0
    ways = 0
    for length in (1, 2):
        token = text[offset : offset + length]
        if len(token) == length and 1 <= int(token) <= 26:
            ways += enumerate_valid_groupings(text, offset + length)
    return ways


@settings(max_examples=100)
@given(st.text(alphabet="0123456789", min_size=1, max_size=14))
def test_rolling_count_matches_recursive_token_groupings(text):
    assert evaluate(FOLDER, args=[text]) == enumerate_valid_groupings(text)

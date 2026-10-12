from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0140-word-break-ii"


def cut_sentences(text, dictionary):
    answers = set()
    for mask in range(1 << (len(text) - 1)):
        parts, start = [], 0
        for end in range(1, len(text)):
            if mask & (1 << (end - 1)):
                parts.append(text[start:end])
                start = end
        parts.append(text[start:])
        if all(word in dictionary for word in parts):
            answers.add(" ".join(parts))
    return answers


@settings(max_examples=80)
@given(
    st.text(alphabet="ab", min_size=1, max_size=9),
    st.lists(st.text(alphabet="ab", min_size=1, max_size=5), min_size=1, max_size=8, unique=True),
)
def test_feasible_backtracking_matches_every_partition_mask(text, dictionary):
    expected = cut_sentences(text, dictionary)
    answer = evaluate(FOLDER, args=[text, dictionary])
    assert len(answer) == len(expected)
    assert set(answer) == expected

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0139-word-break"


def all_cut_partitions(text):
    for mask in range(1 << (len(text) - 1)):
        parts, start = [], 0
        for end in range(1, len(text)):
            if mask & (1 << (end - 1)):
                parts.append(text[start:end])
                start = end
        parts.append(text[start:])
        yield parts


@settings(max_examples=80)
@given(
    st.text(alphabet="ab", min_size=1, max_size=12),
    st.lists(st.text(alphabet="ab", min_size=1, max_size=5), min_size=1, max_size=8, unique=True),
)
def test_prefix_reachability_matches_every_cut_mask(text, dictionary):
    expected = any(all(word in dictionary for word in parts) for parts in all_cut_partitions(text))
    assert evaluate(FOLDER, args=[text, dictionary]) == expected

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0763-partition-labels"


def best_cut_mask(s):
    best = []
    for mask in range(1 << (len(s) - 1)):
        ends = [index + 1 for index in range(len(s) - 1) if mask & (1 << index)] + [len(s)]
        start = 0
        owners = {}
        valid = True
        lengths = []
        for group, end in enumerate(ends):
            for character in s[start:end]:
                if character in owners and owners[character] != group:
                    valid = False
                owners[character] = group
            lengths.append(end - start)
            start = end
        if valid and len(lengths) > len(best):
            best = lengths
    return best


@given(st.text(alphabet="abcd", min_size=1, max_size=9))
def test_earliest_boundaries_match_all_possible_cut_masks(s):
    assert evaluate(FOLDER, args=[s]) == best_cut_mask(s)

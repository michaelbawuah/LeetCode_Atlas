from itertools import product

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0127-word-ladder"


@st.composite
def ladders(draw):
    width = draw(st.integers(1, 3))
    universe = ["".join(chars) for chars in product("abc", repeat=width)]
    first, last = draw(st.lists(st.sampled_from(universe), min_size=2, max_size=2, unique=True))
    dictionary = draw(
        st.lists(
            st.sampled_from(universe), min_size=1, max_size=min(10, len(universe)), unique=True
        )
    )
    return first, last, dictionary


def all_pairs_ladder(begin, end, dictionary):
    if end not in dictionary:
        return 0
    words = list(set(dictionary) | {begin})
    distance = [[0 if i == j else 1000 for j in range(len(words))] for i in range(len(words))]
    for i, first in enumerate(words):
        for j, second in enumerate(words):
            if sum(a != b for a, b in zip(first, second, strict=True)) == 1:
                distance[i][j] = 1
    for via in range(len(words)):
        for first in range(len(words)):
            for last in range(len(words)):
                distance[first][last] = min(
                    distance[first][last], distance[first][via] + distance[via][last]
                )
    length = distance[words.index(begin)][words.index(end)]
    return length + 1 if length < 1000 else 0


@given(ladders())
def test_wildcard_bfs_matches_all_pairs_shortest_paths(case):
    assert evaluate(FOLDER, args=list(case)) == all_pairs_ladder(*case)

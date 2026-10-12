from itertools import product

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "0039-combination-sum"


def multiplicity_oracle(candidates, target):
    answers = set()
    for multiplicities in product(*(range(target // value + 1) for value in candidates)):
        if (
            sum(value * count for value, count in zip(candidates, multiplicities, strict=True))
            == target
        ):
            answers.add(
                tuple(
                    sorted(
                        value
                        for value, count in zip(candidates, multiplicities, strict=True)
                        for _ in range(count)
                    )
                )
            )
    return answers


@given(st.lists(st.integers(2, 9), min_size=1, max_size=4, unique=True), st.integers(1, 16))
def test_backtracking_matches_exhaustive_candidate_multiplicities(candidates, target):
    actual = evaluate(FOLDER, args=[candidates, target])
    expected = multiplicity_oracle(candidates, target)
    assert len(actual) == len(expected)
    assert {tuple(sorted(answer)) for answer in actual} == expected

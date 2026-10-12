from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "1220-count-vowels-permutation"


def oracle(n):
    modulus = 1_000_000_007
    allowed = {"a": "e", "e": "ai", "i": "aeou", "o": "iu", "u": "a"}
    vowels = "aeiou"
    transition = [
        [int(destination in allowed[source]) for source in vowels] for destination in vowels
    ]

    def multiply(left, right):
        return [
            [
                sum(left[row][inner] * right[inner][column] for inner in range(5)) % modulus
                for column in range(5)
            ]
            for row in range(5)
        ]

    power = [[int(row == column) for column in range(5)] for row in range(5)]
    exponent = n - 1
    while exponent:
        if exponent & 1:
            power = multiply(power, transition)
        transition = multiply(transition, transition)
        exponent >>= 1
    return sum(map(sum, power)) % modulus


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.integers(1, 20000)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

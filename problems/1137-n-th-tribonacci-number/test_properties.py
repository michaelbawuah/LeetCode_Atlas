from math import factorial

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import evaluate

FOLDER = "1137-n-th-tribonacci-number"


def oracle(n):
    if n == 0:
        return 0
    target = n - 1
    answer = 0
    for threes in range(target // 3 + 1):
        for twos in range((target - 3 * threes) // 2 + 1):
            ones = target - 3 * threes - 2 * twos
            parts = ones + twos + threes
            answer += factorial(parts) // (factorial(ones) * factorial(twos) * factorial(threes))
    return answer


@settings(max_examples=60, deadline=None)
@given(st.tuples(st.integers(0, 37)))
def test_optimized_matches_independent_small_or_model_oracle(args):
    assert evaluate(FOLDER, args=list(args)) == oracle(*args)

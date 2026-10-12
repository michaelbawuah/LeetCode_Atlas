import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0752-open-the-lock"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_752", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(deadends, target):
    blocked = {int(value) for value in deadends}
    finish = int(target)
    if 0 in blocked or finish in blocked:
        return -1
    front, back = {0}, {finish}
    seen_front, seen_back = {0}, {finish}
    distance = 0
    while front and back:
        if front & back:
            return distance
        if len(front) > len(back):
            front, back = back, front
            seen_front, seen_back = seen_back, seen_front
        following = set()
        for state in front:
            for power in (1, 10, 100, 1000):
                digit = state // power % 10
                for step in (-1, 1):
                    candidate = state + (((digit + step) % 10) - digit) * power
                    if candidate not in blocked and candidate not in seen_front:
                        following.add(candidate)
        front = following
        seen_front.update(front)
        distance += 1
    return -1


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

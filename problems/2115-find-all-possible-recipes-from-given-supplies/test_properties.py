import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "2115-find-all-possible-recipes-from-given-supplies"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_2115", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(recipes, ingredients, supplies):
    available = set(supplies)
    while True:
        following = {
            recipe
            for recipe, items in zip(recipes, ingredients, strict=True)
            if all(item in available for item in items)
        }
        if following <= available:
            break
        available.update(following)
    return [recipe for recipe in recipes if recipe in available]


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

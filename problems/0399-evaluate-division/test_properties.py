import importlib.util
import random
from pathlib import Path

from hypothesis import given, settings
from hypothesis import strategies as st

from atlas.runtime import check_result, evaluate, metadata

FOLDER = "0399-evaluate-division"
spec = importlib.util.spec_from_file_location(
    "atlas_strategy_399", Path(__file__).with_name("parity.py")
)
strategy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(strategy)


def reference(equations, values, queries):
    names = sorted({name for equation in equations for name in equation})
    ratios = {(name, name): 1.0 for name in names}
    for (a, b), value in zip(equations, values, strict=True):
        ratios[a, b] = value
        ratios[b, a] = 1.0 / value
    for via in names:
        for a in names:
            for b in names:
                if (a, via) in ratios and (via, b) in ratios:
                    ratios[a, b] = ratios[a, via] * ratios[via, b]
    return [ratios.get((a, b), -1.0) for a, b in queries]


@settings(max_examples=60)
@given(st.integers(0, 2**32 - 1))
def test_optimized_result_matches_independent_bounded_reference(seed):
    args = strategy.generate(random.Random(seed))
    expected = reference(*args)
    actual = evaluate(FOLDER, args=args)
    assert check_result(metadata(FOLDER), actual, expected, args=args), (args, actual, expected)

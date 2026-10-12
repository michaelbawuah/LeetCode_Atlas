from functools import lru_cache

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0509-fibonacci-number").Solution


@lru_cache(None)
def recursive(n):
    return n if n < 2 else recursive(n - 1) + recursive(n - 2)


@given(st.integers(0, 30))
def test_scalar_recurrence_matches_recursive_definition(n):
    assert Solution().fib(n) == recursive(n)

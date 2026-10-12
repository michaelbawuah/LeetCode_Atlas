from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0496-next-greater-element-i").Solution


@given(values=st.lists(st.integers(0, 10000), min_size=1, max_size=30, unique=True), data=st.data())
def test_stack_matches_direct_forward_search(values, data):
    queries = data.draw(
        st.lists(st.sampled_from(values), min_size=1, max_size=len(values), unique=True)
    )
    expected = [
        next((other for other in values[values.index(value) + 1 :] if other > value), -1)
        for value in queries
    ]
    assert Solution().nextGreaterElement(queries, values) == expected

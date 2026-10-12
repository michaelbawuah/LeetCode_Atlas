from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

MinStack = load_module("0155-min-stack").MinStack


@given(st.lists(st.integers(-(2**31), 2**31 - 1), min_size=1, max_size=80))
def test_interleaved_operations_match_plain_list(actions):
    stack = MinStack()
    values = []
    for action in actions:
        operation = action % 4
        if not values or operation == 0:
            assert stack.push(action) is None
            values.append(action)
        elif operation == 1:
            assert stack.pop() is None
            values.pop()
        elif operation == 2:
            assert stack.top() == values[-1]
        else:
            assert stack.getMin() == min(values)
        if values:
            assert stack.top() == values[-1]
            assert stack.getMin() == min(values)


@given(st.lists(st.integers(-20, 20), min_size=1, max_size=50))
def test_each_pop_restores_previous_minimum(values):
    stack = MinStack()
    reference = []
    for value in values:
        stack.push(value)
        reference.append(value)
        assert stack.getMin() == min(reference)
    while reference:
        assert stack.top() == reference[-1]
        assert stack.getMin() == min(reference)
        assert stack.pop() is None
        reference.pop()

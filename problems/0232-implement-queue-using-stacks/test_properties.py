from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

MyQueue = load_module("0232-implement-queue-using-stacks").MyQueue


@given(st.lists(st.tuples(st.integers(0, 3), st.integers(1, 9)), min_size=1, max_size=100))
def test_stack_queue_matches_plain_fifo(actions):
    obj = MyQueue()
    values = []
    for operation, value in actions:
        if operation == 0 or not values:
            values.append(value)
            assert obj.push(value) is None
        elif operation == 1:
            assert obj.pop() == values.pop(0)
        elif operation == 2:
            assert obj.peek() == values[0]
        else:
            assert obj.empty() == (not values)
        assert obj.empty() == (not values)

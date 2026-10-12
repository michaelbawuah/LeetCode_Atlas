from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

MyStack = load_module("0225-implement-stack-using-queues").MyStack


@given(st.lists(st.tuples(st.integers(0, 3), st.integers(1, 9)), min_size=1, max_size=80))
def test_queue_stack_matches_list(actions):
    obj = MyStack()
    values = []
    for operation, value in actions:
        if operation == 0 or not values:
            values.append(value)
            assert obj.push(value) is None
        elif operation == 1:
            assert obj.pop() == values.pop()
        elif operation == 2:
            assert obj.top() == values[-1]
        else:
            assert obj.empty() == (not values)
        assert obj.empty() == (not values)

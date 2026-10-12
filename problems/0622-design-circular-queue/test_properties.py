from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

MyCircularQueue = load_module("0622-design-circular-queue").MyCircularQueue


@given(
    capacity=st.integers(1, 8),
    actions=st.lists(st.tuples(st.integers(0, 5), st.integers(0, 1000)), min_size=1, max_size=100),
)
def test_circular_histories_match_plain_list(capacity, actions):
    obj = MyCircularQueue(capacity)
    model = []
    for operation, value in actions:
        if operation == 0:
            expected = len(model) < capacity
            if expected:
                model.append(value)
            assert obj.enQueue(value) == expected
        elif operation == 1:
            expected = bool(model)
            if expected:
                model.pop(0)
            assert obj.deQueue() == expected
        elif operation == 2:
            assert obj.Front() == (model[0] if model else -1)
        elif operation == 3:
            assert obj.Rear() == (model[-1] if model else -1)
        elif operation == 4:
            assert obj.isEmpty() == (not model)
        elif operation == 5:
            assert obj.isFull() == (len(model) == capacity)
        assert obj.isEmpty() == (not model)
        assert obj.isFull() == (len(model) == capacity)

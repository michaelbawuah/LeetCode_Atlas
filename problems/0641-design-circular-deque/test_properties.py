from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

MyCircularDeque = load_module("0641-design-circular-deque").MyCircularDeque


@given(
    capacity=st.integers(1, 8),
    actions=st.lists(st.tuples(st.integers(0, 7), st.integers(0, 1000)), min_size=1, max_size=100),
)
def test_circular_histories_match_plain_list(capacity, actions):
    obj = MyCircularDeque(capacity)
    model = []
    for operation, value in actions:
        if operation == 0:
            expected = len(model) < capacity
            if expected:
                model.append(value)
            assert obj.insertLast(value) == expected
        elif operation == 1:
            expected = bool(model)
            if expected:
                model.pop(0)
            assert obj.deleteFront() == expected
        elif operation == 2:
            assert obj.getFront() == (model[0] if model else -1)
        elif operation == 3:
            assert obj.getRear() == (model[-1] if model else -1)
        elif operation == 4:
            assert obj.isEmpty() == (not model)
        elif operation == 5:
            assert obj.isFull() == (len(model) == capacity)
        elif operation == 6 and True:
            expected = len(model) < capacity
            if expected:
                model.insert(0, value)
            assert obj.insertFront(value) == expected
        elif operation == 7 and True:
            expected = bool(model)
            if expected:
                model.pop()
            assert obj.deleteLast() == expected
        assert obj.isEmpty() == (not model)
        assert obj.isFull() == (len(model) == capacity)

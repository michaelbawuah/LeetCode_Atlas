from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

MyHashSet = load_module("0705-design-hashset").MyHashSet


@given(st.lists(st.tuples(st.integers(0, 2), st.integers(0, 1000000)), min_size=1, max_size=100))
def test_complete_set_histories_match_standard_set(actions):
    obj = MyHashSet()
    model = set()
    for action, key in actions:
        if action == 0:
            model.add(key)
            assert obj.add(key) is None
        elif action == 1:
            model.discard(key)
            assert obj.remove(key) is None
        else:
            assert obj.contains(key) == (key in model)
    for key in model:
        assert obj.contains(key) is True

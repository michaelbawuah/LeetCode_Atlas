from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

MyHashMap = load_module("0706-design-hashmap").MyHashMap


@given(
    st.lists(
        st.tuples(st.integers(0, 2), st.integers(0, 1000000), st.integers(0, 1000000)),
        min_size=1,
        max_size=100,
    )
)
def test_complete_map_histories_match_dictionary(actions):
    obj = MyHashMap()
    model = {}
    for action, key, value in actions:
        if action == 0:
            model[key] = value
            assert obj.put(key, value) is None
        elif action == 1:
            model.pop(key, None)
            assert obj.remove(key) is None
        else:
            assert obj.get(key) == model.get(key, -1)
    for key, value in model.items():
        assert obj.get(key) == value

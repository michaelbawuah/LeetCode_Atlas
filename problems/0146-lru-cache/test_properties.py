from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

LRUCache = load_module("0146-lru-cache").LRUCache


@given(
    capacity=st.integers(1, 5),
    actions=st.lists(
        st.tuples(st.booleans(), st.integers(0, 8), st.integers(0, 100)), min_size=1, max_size=100
    ),
)
def test_accesses_match_plain_recency_list(capacity, actions):
    cache = LRUCache(capacity)
    order = []
    values = {}
    for write, key, value in actions:
        if write:
            if key in order:
                order.remove(key)
            order.append(key)
            values[key] = value
            if len(order) > capacity:
                del values[order.pop(0)]
            assert cache.put(key, value) is None
        else:
            expected = values.get(key, -1)
            if key in order:
                order.remove(key)
                order.append(key)
            assert cache.get(key) == expected

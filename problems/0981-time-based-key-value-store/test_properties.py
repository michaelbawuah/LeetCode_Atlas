from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

TimeMap = load_module("0981-time-based-key-value-store").TimeMap


@given(
    actions=st.lists(
        st.tuples(
            st.booleans(),
            st.sampled_from(["a", "b", "c"]),
            st.text(alphabet="abc012", min_size=1, max_size=6),
            st.integers(1, 200),
        ),
        min_size=1,
        max_size=100,
    )
)
def test_queries_match_linear_history(actions):
    store = TimeMap()
    records = []
    clock = 0
    for write, key, value, query in actions:
        if write:
            clock += 1
            records.append((key, value, clock))
            assert store.set(key, value, clock) is None
        else:
            eligible = [
                value for old_key, value, time in records if old_key == key and time <= query
            ]
            assert store.get(key, query) == (eligible[-1] if eligible else "")

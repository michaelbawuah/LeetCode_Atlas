from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

SnapshotArray = load_module("1146-snapshot-array").SnapshotArray


@given(
    length=st.integers(1, 10),
    actions=st.lists(
        st.tuples(st.integers(0, 2), st.integers(0, 100), st.integers(0, 100)),
        min_size=1,
        max_size=100,
    ),
)
def test_histories_match_full_snapshot_copies(length, actions):
    obj = SnapshotArray(length)
    current = [0] * length
    copies = []
    for operation, index, value in actions:
        index %= length
        if operation == 0:
            current[index] = value
            assert obj.set(index, value) is None
        elif operation == 1 or not copies:
            copies.append(list(current))
            assert obj.snap() == len(copies) - 1
        else:
            id = value % len(copies)
            assert obj.get(index, id) == copies[id][index]

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

NumArray = load_module("0307-range-sum-query-mutable").NumArray


@given(
    nums=st.lists(st.integers(-1000, 1000), min_size=1, max_size=30),
    actions=st.lists(
        st.tuples(st.booleans(), st.integers(0, 29), st.integers(-1000, 1000)),
        min_size=1,
        max_size=80,
    ),
)
def test_updates_and_queries_match_plain_array(nums, actions):
    values = list(nums)
    snapshot = list(nums)
    obj = NumArray(nums)
    for update, index, value in actions:
        index %= len(values)
        if update:
            values[index] = value
            assert obj.update(index, value) is None
        else:
            right = abs(value) % len(values)
            left, right = sorted((index, right))
            assert obj.sumRange(left, right) == sum(values[left : right + 1])
    assert nums == snapshot

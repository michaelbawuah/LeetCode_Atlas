from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

KthLargest = load_module("0703-kth-largest-element-in-a-stream").KthLargest


@given(
    initial=st.lists(st.integers(-10000, 10000), max_size=30),
    additions=st.lists(st.integers(-10000, 10000), min_size=1, max_size=40),
    data=st.data(),
)
def test_each_addition_matches_full_stream_sort(initial, additions, data):
    k = data.draw(st.integers(1, len(initial) + 1))
    snapshot = list(initial)
    stream = KthLargest(k, initial)
    observed = list(initial)
    for value in additions:
        observed.append(value)
        expected = sorted(observed, reverse=True)[k - 1]
        assert stream.add(value) == expected
    assert initial == snapshot

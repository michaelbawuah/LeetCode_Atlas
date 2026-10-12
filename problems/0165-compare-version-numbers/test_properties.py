from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0165-compare-version-numbers").Solution


@given(
    a=st.lists(st.integers(0, 10000), min_size=1, max_size=12),
    b=st.lists(st.integers(0, 10000), min_size=1, max_size=12),
)
def test_version_order_matches_padded_numeric_tuples(a, b):
    length = max(len(a), len(b))
    first = tuple(a + [0] * (length - len(a)))
    second = tuple(b + [0] * (length - len(b)))
    expected = (first > second) - (first < second)
    assert (
        Solution().compareVersion(".".join("00" + str(x) for x in a), ".".join(str(x) for x in b))
        == expected
    )

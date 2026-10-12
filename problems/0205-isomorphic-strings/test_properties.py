from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0205-isomorphic-strings").Solution


@given(length=st.integers(1, 50), data=st.data())
def test_bijection_matches_pairwise_equality_pattern(length, data):
    a = data.draw(st.text(alphabet="abc12!", min_size=length, max_size=length))
    b = data.draw(st.text(alphabet="xyz45?", min_size=length, max_size=length))
    expected = all((a[i] == a[j]) == (b[i] == b[j]) for i in range(length) for j in range(length))
    assert Solution().isIsomorphic(a, b) == expected

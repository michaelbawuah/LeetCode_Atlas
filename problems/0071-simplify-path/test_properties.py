import posixpath

from hypothesis import given
from hypothesis import strategies as st

from atlas.runtime import load_module

Solution = load_module("0071-simplify-path").Solution


@given(
    parts=st.lists(st.sampled_from(["a", "b", ".", "..", "...", "x.y", ".hidden"]), max_size=30),
    separator=st.sampled_from(["/", "//", "///"]),
)
def test_path_matches_posix_normalization(parts, separator):
    path = separator + separator.join(parts) + separator
    expected = "/" + posixpath.normpath(path).lstrip("/")
    assert Solution().simplifyPath(path) == expected

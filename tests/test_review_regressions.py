"""Check ordering freedom promised by the actual problem specifications."""

from atlas.runtime import check_result, metadata


def test_two_sum_accepts_either_pair_order_without_accepting_a_reused_index():
    meta = metadata("0001-two-sum")
    assert check_result(meta, [1, 0], [0, 1])
    assert not check_result(meta, [0, 0], [0, 1])
    assert not check_result(meta, [0, 1, 1], [0, 1])


def test_three_sum_accepts_inner_and_outer_ordering_but_preserves_multiplicity():
    meta = metadata("0015-3sum")
    expected = [[-1, 0, 1], [0, 0, 0]]
    assert check_result(meta, [[0, 0, 0], [1, -1, 0]], expected)
    assert not check_result(meta, [[-1, 0, 1], [-1, 0, 1]], expected)
    assert not check_result(meta, [[-1, 0, 1], [0, 0]], expected)
    assert not check_result(meta, [[-1, 0, 1], [0, 0, 0], [1, 0, -1]], expected)

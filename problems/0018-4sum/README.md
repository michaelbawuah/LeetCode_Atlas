# 18 · 4Sum

[Problem](https://leetcode.com/problems/4sum/) · Medium · Sorting and two pointers

## Approach

**Baseline:** enumerate all four-index combinations and deduplicate their values:
O(n⁴) time.
**Chosen approach:** sort a copy, fix two distinct anchor positions, and use two
pointers for the remaining pair. Skip duplicate anchor and partner values.

## Invariant and correctness

For each anchor pair, sorted order makes a too-small total safely discard the
left endpoint, since all other remaining partners for it give an equal or smaller
total. A too-large total safely discards the right endpoint by the symmetric
argument. All matches for that pair are therefore found. Distinct positions ensure
four different indices; skipping repeated values prevents duplicate value quadruplets.

## Complexity

O(n³) time and O(n) auxiliary space for the sorted copy and sorting workspace,
excluding up to O(n³) output. Python integers handle the large intermediate sums
without fixed-width overflow. The input is preserved.

## Verification and pitfalls

Properties enumerate all four-position combinations. Fixtures cover fewer than
four values, repeated zeroes, repeated partners, and ±10⁹ values. A sum of four
valid inputs can exceed signed 32-bit range; wrapping must not create a false match.
The checker ignores both quadruplet ordering and result-list ordering while
preserving duplicate multiplicity, so duplicate answers still fail.

**Follow-up:** how would recursive k-sum share the same two-pointer base case?

## C++23 counterpart

C++ also sorts a copy and skips duplicate anchor and partner values. Each sum widens its first term to `std::int64_t` before addition: four valid ±10⁹ inputs can reach ±4×10⁹ and overflow signed 32-bit arithmetic. The existing wraparound fixture catches a false match caused by that mistake. O(n) auxiliary storage excludes the up-to-O(n³) output; input is preserved.

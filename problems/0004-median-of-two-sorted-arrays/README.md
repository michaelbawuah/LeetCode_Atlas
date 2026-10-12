# 4 · Median of Two Sorted Arrays

[Problem](https://leetcode.com/problems/median-of-two-sorted-arrays/) · Hard · Binary-search partition

## Approach

**Baseline:** merge both sorted arrays in O(m + n) time and read the middle.
**Chosen approach:** binary-search a cut in the shorter array. Choose the other
cut so the left side contains half the combined elements, rounded upward.
Sentinel infinities represent missing values at an array boundary.

## Invariant and correctness

Each array is already internally ordered. A partition is globally ordered
exactly when each left boundary is no greater than the opposite right boundary.
If the shorter array's left boundary is too large, its cut must move left;
if the other left boundary is too large, it must move right. These comparisons
preserve the valid partition in the search range. An ordered partition gives
the median as the largest left value, or the average of the two middle boundaries.

## Complexity

O(log(min(m, n) + 1)) time and O(1) auxiliary space. Swapping array references
copies no data. The `+ 1` expression also covers an empty shorter array.

## Verification and pitfalls

Tests compare against sorting the combined input, covering empty arrays,
duplicates, odd/even totals, and extreme cuts. The combined length must be nonzero.
Return a float consistently; do not accidentally use integer division.

**Follow-up:** how would a partition search find an arbitrary kth element?

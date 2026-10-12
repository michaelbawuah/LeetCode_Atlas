# 164 · Maximum Gap

[Problem](https://leetcode.com/problems/maximum-gap/) · Medium

## Idea and approaches

Group values into narrow numeric buckets, retaining only each bucket minimum and maximum. Sorting is an O(n log n) baseline; the required linear bound comes from the spacing lower bound.

## Correctness invariant

For range R and n values, some sorted adjacent gap is at least R/(n - 1). Choose bucket width max(1, floor(R/(n - 1))). Every within-bucket gap is smaller than that width and therefore smaller than the possible maximum. The maximum must occur between consecutive nonempty buckets, whose minimum-minus-previous-maximum is examined. Equal-valued and singleton arrays are handled separately.

## Complexity

O(n) time and O(n) auxiliary space. The bucket count is at most a constant multiple of n: small R gives at most n buckets, and otherwise the floored width gives fewer than roughly 2n. Input is preserved.

## Verification and pitfalls

Tests compare against sorted adjacent differences, with duplicates, huge numeric ranges, and unit spacing.

Allocating one slot per possible value would be enormous for a 10^9 range. Empty buckets must be skipped when tracking the previous maximum.

**Follow-up:** How would fixed-width radix sorting provide another linear-time approach?

# 16 · 3Sum Closest

[Problem](https://leetcode.com/problems/3sum-closest/) · Medium · Sorting and two pointers

## Approach

**Baseline:** enumerate all index triples and retain the closest sum: O(n³) time.
**Chosen approach:** sort a copy, fix each anchor, and walk two pointers over its
suffix. Update the best distance before moving a pointer; return immediately on an exact match.

## Invariant and correctness

For a fixed anchor, a sum below target can be improved only by increasing it.
Any remaining pair using the same left endpoint and a smaller right endpoint
would be no larger and cannot improve upon the sum just checked, so discarding
that left endpoint is safe. A symmetric argument applies above target. Thus
every skipped pair is dominated by a checked pair, and the best sum over all
anchors is globally closest. The problem guarantees an unambiguous answer.

## Complexity

O(n²) time and O(n) auxiliary space for Python's sorted copy and sorting workspace.
The input remains unchanged; the output is a scalar.

## Verification and pitfalls

The independent oracle enumerates triple sums and keeps generated cases with a
unique closest sum. Cover targets outside all attainable sums, negatives, repeated
values, and exact matches. Compare absolute distance rather than signed difference.
Pointer motion depends on whether the sum is above or below target.

**Follow-up:** what pruning bounds can skip anchors whose entire attainable range is too far away?

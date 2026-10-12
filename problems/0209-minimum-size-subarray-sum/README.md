# 209 · Minimum Size Subarray Sum

[Problem](https://leetcode.com/problems/minimum-size-subarray-sum/) · Medium · Sliding window

## Idea

All values are positive, so moving the right edge increases the sum and moving
the left edge decreases it. This monotonicity makes a shrinking window possible.

**Baseline:** enumerate all starting and ending positions with rolling sums:
O(n²) time.
**Chosen approach:** extend the right edge, then repeatedly record valid lengths
and remove the leftmost value while the sum still meets the target.

## Why it works

The maintained total is exactly the current window sum. For each right endpoint,
shrinking visits valid windows in decreasing length until the sum falls below
target, recording the shortest valid one at that endpoint. A discarded left
endpoint already produced a valid answer; extending it later would only make
that window longer. Therefore it cannot produce a better answer in the future.
Taking the smallest recorded length covers the optimum.

## Complexity

O(n) time and O(1) auxiliary space. Each value is added once and removed at most once.

## Tests and pitfalls

Fixtures cover unreachable targets, a full-array answer, a singleton answer, and
late improvements. The oracle enumerates all nonempty contiguous slices.
Use a `while` loop when shrinking: one removal may leave further shorter valid
windows. The proof depends on positive input values; negative values require
a different algorithm.

**Follow-up:** which prefix-sum and deque technique handles negative values?

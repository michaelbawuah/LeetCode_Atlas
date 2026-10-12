# 643 · Maximum Average Subarray I

[Problem](https://leetcode.com/problems/maximum-average-subarray-i/) · Easy

## Idea and approaches

Compare integer sums of fixed-width windows and divide the largest once. Summing every window independently is the O(nk) baseline.

## Correctness invariant

The running total equals the current k-element window sum. Moving the right boundary adds the entering value and subtracts exactly the departing value, maintaining that invariant. All windows have the same positive divisor, so maximizing their sums also maximizes their averages.

## Complexity

O(n) time and O(1) auxiliary space. Initial summation uses a generator rather than a copied slice; output is one float.

## Verification and pitfalls

Tests independently sum each window and use the configured approximate comparison. Negative averages, k = 1, k = n, and opposite numeric bounds are named cases.

Initialize best from the first real window rather than zero, which would fail on all-negative arrays.

**Follow-up:** How does finding a maximum average change when window length is only bounded below?

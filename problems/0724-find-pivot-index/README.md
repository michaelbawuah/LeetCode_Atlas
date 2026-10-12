# 724 · Find Pivot Index

[Problem](https://leetcode.com/problems/find-pivot-index/) · Easy

## Idea and approaches

Keep the sum strictly left of the current index and derive the right sum from the whole-array total. Summing both sides for every index is the O(n^2) baseline.

## Correctness invariant

Before checking index i, left equals the sum of values with smaller indices. The right sum is total - left - nums[i]. Equality therefore exactly identifies a pivot. Checking before adding the current value maintains strict sides, and scanning left-to-right returns the required earliest pivot.

## Complexity

O(n) time and O(1) auxiliary space. Input is preserved and signed values need no monotonicity assumption.

## Verification and pitfalls

Tests independently sum slices on each side and select the first matching index. Cases cover endpoint pivots, several valid pivots, negative totals, and no answer.

The current element belongs to neither side. A singleton always has pivot zero because both side sums are empty.

**Follow-up:** How would a point-update data structure answer whether one given index is a pivot?

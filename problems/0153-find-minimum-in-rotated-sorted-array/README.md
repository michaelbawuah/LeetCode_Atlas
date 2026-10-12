# 153 · Find Minimum in Rotated Sorted Array

[LeetCode problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Intuition
Compare the middle value with the right boundary. A larger middle value puts the rotation drop to its right; otherwise the minimum is at the middle or to its left.

## Baseline and approach
A linear scan finds the minimum in O(n) time. Binary search keeps a closed interval containing it and halves that interval until only one index remains. Distinct values are required by this version of the problem.

## Why it works
If `nums[mid] > nums[right]`, the minimum lies strictly after `mid`. Otherwise the segment from `mid` to `right` is ordered, so the minimum cannot lie strictly after `mid`. Both updates preserve the minimum in the remaining interval, and the interval strictly shrinks.

## Complexity
For n values: **O(log n) time, O(1) auxiliary space**.

## Pitfalls
Do not discard `mid` when moving the right boundary: it might be the minimum. An already sorted array and a one-element array still follow the same invariant.

## Follow-up
How do duplicate values weaken the strict comparison, and why can the worst case become linear?

# 515 · Find Largest Value in Each Tree Row

[LeetCode problem](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)

## Intuition
A level frontier separates the values contributing to each maximum.

## Baseline and approach
Collecting all depth groups works but retains O(n) values. Compute one maximum while consuming each BFS level.

## Why it works
The queue begins each round with exactly one level. Initializing from a real node handles negative-only rows. Processing its fixed size examines every value in that row and schedules only the following row, so the appended maximum is exact.

## Complexity
**O(n) time; O(w) auxiliary; O(h) output space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Zero is an invalid initial maximum for a negative-only level. Distinguish O(h) output rows from O(w) frontier storage.

## Follow-up
Compute minimum, maximum, and average together in one traversal.

## Python and C++23
Both versions initialize each level maximum from an actual value, preserving correctness for negative values including INT_MIN. No input links or values are changed.

C++23 submission-method complexity: **O(n) time; O(w) auxiliary; O(h) output space**. Adapter ownership and JSON conversion are separate.

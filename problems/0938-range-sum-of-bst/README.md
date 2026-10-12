# 938 · Range Sum of BST

[LeetCode problem](https://leetcode.com/problems/range-sum-of-bst/)

## Intuition
BST ordering can rule out an entire subtree beyond one range boundary.

## Baseline and approach
A full traversal with a value filter works in O(n). Prune the left side when its values must be too small, and the right side when they must be too large.

## Why it works
At a node no larger than low, every left value is below low; the mirrored rule holds at high. Skipping those subtrees loses no qualifying key. Every visited value inside the inclusive range contributes once.

## Complexity
**O(n) worst case time; O(h) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Boundary values are included. Pruning improves many inputs but worst-case time remains O(n) when the range covers the tree.

## Follow-up
Answer repeated range sums using subtree totals and two prefix-sum queries.

## Python and C++23
Both implementations prune subtrees using strict BST bounds. C++ accumulates in long long and returns int under the unique positive-key and bounded node-count contract. A full-range query still takes O(n) time; all input links and values are unchanged.

C++23 submission-method complexity: **O(n) worst case time; O(h) space**. Adapter ownership and JSON conversion are separate.

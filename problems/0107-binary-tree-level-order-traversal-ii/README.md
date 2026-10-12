# 107 · Binary Tree Level Order Traversal II

[LeetCode problem](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

## Intuition
Level order within a row stays unchanged; only the order of completed rows changes.

## Baseline and approach
Repeatedly inserting each row at the front of a Python list can shift existing rows. Collect ordinary BFS rows and reverse the outer list once.

## Why it works
BFS creates rows in increasing depth, with left-to-right node order. Reversing the outer list changes increasing depth to decreasing depth while leaving every row intact.

## Complexity
**O(n) time; O(w) auxiliary; O(n) output space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Reverse the rows, not their contents. A fixed queue size separates children from their parents.

## Follow-up
Stream levels from a precomputed depth index and explain why bottom-up streaming generally needs prior knowledge of the tree.

## Python and C++23
Both versions reverse the outer collection after ordinary BFS. Rows retain their original left-to-right values, and borrowed tree nodes remain unchanged.

C++23 submission-method complexity: **O(n) time; O(w) auxiliary; O(n) output space**. Adapter ownership and JSON conversion are separate.

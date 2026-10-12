# 108 · Convert Sorted Array to Binary Search Tree

[LeetCode problem](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

## Intuition
Choosing a midpoint leaves subarrays whose sizes differ by at most one.

## Baseline and approach
Inserting sorted values one at a time creates a chain. Midpoint subdivision places a central key at each subtree root and builds its two ranges directly.

## Why it works
Every left-range value is smaller than its midpoint and every right-range value is larger, establishing strict BST ordering. The two range sizes differ by at most one, so recursively applying the same split bounds their heights and produces a balanced tree.

## Complexity
**O(n) time; O(log(n + 1)) auxiliary; O(n) output space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
There can be several correct balanced shapes. The semantic checker compares inorder values and balance rather than one chosen midpoint convention. Index ranges avoid copied slices.

## Follow-up
Build a balanced BST from a sorted linked list while avoiding repeated midpoint scans.

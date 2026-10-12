# 538 · Convert BST to Greater Tree

[LeetCode problem](https://leetcode.com/problems/convert-bst-to-greater-tree/)

## Intuition
Reverse inorder makes the sum of all greater values available before visiting a node.

## Baseline and approach
Summing greater values independently for each node costs O(n²). One descending traversal keeps a running total and changes the node value in place.

## Why it works
Reverse inorder visits original keys from greatest to smallest. Before a visit, total contains exactly the already visited greater keys; adding the current original key produces the required greater-or-equal sum. Traversal follows links, so changed values cannot alter its order.

## Complexity
**O(n) time; O(h) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Include the current key in the replacement. Negative keys still participate in the running sum. Reuse original nodes and preserve every child link.

## Follow-up
Return a fresh greater-tree copy instead of mutating the original and account for output allocation.

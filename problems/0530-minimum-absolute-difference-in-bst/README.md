# 530 · Minimum Absolute Difference in BST

[LeetCode problem](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

## Intuition
The smallest gap in a sorted sequence occurs between consecutive values.

## Baseline and approach
Comparing all node pairs takes O(n²). BST inorder produces sorted values incrementally, letting each visit compare only with the preceding one.

## Why it works
For any two nonadjacent sorted values, their difference is a sum of intervening nonnegative gaps and cannot be smaller than all those adjacent gaps. Taking the minimum adjacent inorder gap therefore equals the all-pairs minimum.

## Complexity
**O(n) time; O(h) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
The input has at least two unique BST values. Use an explicit absent-previous marker so zero is treated as data. A non-BST inorder sequence would not support this reasoning.

## Follow-up
Maintain the minimum gap dynamically as values are inserted into an ordered set.

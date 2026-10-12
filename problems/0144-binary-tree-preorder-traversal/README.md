# 144 · Binary Tree Preorder Traversal

[LeetCode problem](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## Intuition
Preorder means visiting the node itself, then its complete left subtree, then its complete right subtree.

## Baseline and approach
Recursive DFS directly follows that definition. An explicit stack produces the same order: record a popped node, then push its right child before its left child so the left subtree is processed first.

## Why it works
The next stack entry is the next node in preorder. Recording it before scheduling its children places the parent before both subtrees. Last-in, first-out scheduling exhausts the left subtree before the pending right subtree, preserving the required order inductively.

## Complexity
For n nodes and height h: **O(n) time, O(h) auxiliary space**, plus **O(n) output storage**.

## Pitfalls
Pushing left before right reverses the subtree visit order. Repeated values still represent distinct nodes and must not be deduplicated.

## Follow-up
Morris traversal can reduce auxiliary storage to O(1). What temporary changes does it make to tree links, and how are those changes restored?

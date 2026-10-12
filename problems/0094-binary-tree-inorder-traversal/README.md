# 94 · Binary Tree Inorder Traversal

[LeetCode problem](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## Intuition
A node is ready to visit only after its entire left region has been visited.

## Baseline and approach
Recursive inorder follows the definition directly. An explicit ancestor stack reproduces its return points: descend left, pop and visit, then descend into the right subtree.

## Why it works
The stack holds ancestors waiting for their inorder visit. When no current left node remains, its top has no unvisited left region, so it is the next inorder node. Visiting it and moving right preserves the left-node-right ordering until all nodes are exhausted.

## Complexity
**O(n) time; O(h) auxiliary; O(n) output space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Pushing is not visiting. Equal values still belong to separate nodes and must remain in the output. Inorder is sorted only when the input is a BST.

## Follow-up
Use temporary predecessor threads for Morris traversal and explain how every changed link is restored.

## Python and C++23
Python lists and C++ vectors hold the pending ancestors. Both traversals leave borrowed tree nodes unchanged and allocate O(n) output values, separate from their O(h) stack space.

C++23 submission-method complexity: **O(n) time; O(h) auxiliary; O(n) output space**. Adapter ownership and JSON conversion costs are separate.

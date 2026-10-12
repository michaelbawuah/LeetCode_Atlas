# 124 · Binary Tree Maximum Path Sum

[LeetCode problem](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

## Intuition
A path may join two child branches at a node, but a path passed upward may retain only one branch.

## Baseline and approach
Enumerating all endpoint pairs is quadratic. Postorder DP stores the best upward path gain for each node and separately tests the path that joins both useful child gains through it.

## Why it works
Once child gains are known, negative gains can only reduce a path and are replaced by zero. A path whose highest node is the current node uses at most its left and right gains, so their sum plus its value is the best such candidate. The upward gain chooses only one side to avoid branching. Every nonempty path has one highest node, so the global maximum considers it.

## Complexity
**O(n) time; O(n) space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Do not return both child gains upward: that would form a branching structure rather than a path. Initialize the best answer from a real node so all-negative trees cannot incorrectly produce zero.

## Follow-up
Recover the actual maximum path while maintaining the same distinction between a joining candidate and an upward gain.

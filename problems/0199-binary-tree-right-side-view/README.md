# 199 · Binary Tree Right Side View

[LeetCode problem](https://leetcode.com/problems/binary-tree-right-side-view/)

## Intuition
At each depth, the first node reached by a right-first traversal is the rightmost existing node at that level.

## Baseline and approach
BFS can retain the last value of each level with O(w) queue space. This solution uses iterative right-first DFS and records a value only when it reaches a depth not seen before. Pushing the left child before the right child makes the right child pop first.

## Why it works
DFS explores every right subtree before its corresponding left subtree. For any fixed depth, this ordering reaches nodes from right to left. The first visited node at that depth is therefore the visible one, even when the left subtree extends deeper than the right.

## Complexity
For n nodes and height h: **O(n) time, O(h) auxiliary space**, plus **O(h) output storage**.

## Pitfalls
Following only right-child links misses deeper visible nodes in left subtrees. The stack is last-in, first-out, so push order must be the reverse of visit order.

## Follow-up
Produce both the left and right views in one level-order traversal.

## Python and C++23
Both versions visit right regions first and keep the first value seen at each depth. The C++ depth type matches vector size comparisons. Neither method changes the borrowed tree links.

C++23 submission-method complexity: **O(n) time; O(h) auxiliary; O(h) output space**. Adapter ownership and JSON conversion costs are separate.

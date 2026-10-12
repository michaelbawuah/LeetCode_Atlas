# 226 · Invert Binary Tree

[LeetCode problem](https://leetcode.com/problems/invert-binary-tree/)

## Intuition
A mirror image swaps left and right at every node, including the nodes below the root.

## Baseline and approach
Recursive swapping is concise. An explicit DFS stack visits each node once and swaps its children in place, avoiding call-stack dependence. It returns the original root reference; the platform supplies `TreeNode`.

## Why it works
Each node is visited exactly once and has its two child links exchanged. Every original edge therefore changes its left/right direction, while node values and parent relationships remain intact. That is precisely the mirrored tree.

## Complexity
For n nodes and height h: **O(n) time, O(h) auxiliary space**. Existing nodes are reused.

## Pitfalls
Swapping only the root mirrors the first level, not the entire tree. After swapping, visit both resulting children exactly once.

## Follow-up
Inverting twice should restore the original tree. Which parts of that claim require checking identity as well as values?

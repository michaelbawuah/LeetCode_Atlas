# 654 · Maximum Binary Tree

[LeetCode problem](https://leetcode.com/problems/maximum-binary-tree/)

## Intuition
A decreasing stack tracks the unfinished right spine of the maximum tree.

## Baseline and approach
Finding a maximum and slicing each remaining range can cost O(n²). A new value replaces every smaller pending right-spine node and attaches their combined subtree on its left.

## Why it works
The stack is a decreasing chain representing the prefix tree's right spine. Popped smaller nodes must belong to the new node's left region; the final popped root already contains earlier popped nodes. The remaining larger ancestor receives the new node as its right child. This preserves inorder input order and maximum-parent ordering.

## Complexity
**O(n) time; O(h) auxiliary; O(n) output space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Values are unique. Every node is pushed and popped at most once, giving amortized linear time. The returned nodes are new and inputs remain unchanged.

## Follow-up
Construct the corresponding minimum Cartesian tree and compare the stack inequality.

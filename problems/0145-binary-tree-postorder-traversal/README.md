# 145 · Binary Tree Postorder Traversal

[LeetCode problem](https://leetcode.com/problems/binary-tree-postorder-traversal/)

## Intuition
Delay each parent until both child regions have been completed.

## Baseline and approach
Recursive postorder naturally returns after both children. Enter/ready stack frames reproduce that timing iteratively: schedule the parent's ready frame below its right and left children.

## Why it works
Each entering node schedules one future ready frame. Last-in, first-out processing completes its left subtree, then its right subtree, before that frame records the parent. Thus each node appears exactly once in left-right-node order.

## Complexity
**O(n) time; O(h) auxiliary; O(n) output space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Record values on the ready visit, not the initial visit. Push right before left so the left region runs first. Do not confuse a reversed preorder trick with direct child-before-parent processing.

## Follow-up
Implement postorder with one stack and a last-visited pointer, comparing its state with the explicit ready flag.

# 98 · Validate Binary Search Tree

[LeetCode problem](https://leetcode.com/problems/validate-binary-search-tree/)

## Intuition
The inorder traversal of a strict binary search tree is strictly increasing. It exposes violations of ancestor bounds as well as immediate-parent ordering.

## Baseline and approach
Checking only each parent-child pair is insufficient. Propagating allowable value bounds is a valid alternative. This implementation walks inorder with an explicit stack and compares each value to the previously visited value.

## Why it works
A strict BST's left subtree values precede and are smaller than its root, while right subtree values follow and are larger. Inductively, its inorder sequence is strictly increasing. Conversely, a strictly increasing inorder sequence places every left-subtree value below its root and every right-subtree value above it, establishing the BST condition at every node.

## Complexity
For n nodes and height h: **O(n) time, O(h) auxiliary space**.

## Pitfalls
Duplicates are invalid. Local parent comparisons miss values that violate a more distant ancestor. `None` denotes the absence of a previous value, so zero and the smallest allowed integer remain valid data.

## Follow-up
How would validation change if equal keys were allowed only in right subtrees?

## Python and C++23 comparison

Both sources use iterative inorder traversal rather than recursive calls. C++ stores ancestor pointers in a vector: O(n) time and O(h) auxiliary space for n nodes and height h. A separate `have_previous` flag distinguishes the first visited value, allowing the full `int` range without reserving an integer sentinel. The traversal borrows nodes owned by the judge or `TreeArena`; it neither changes their links nor allocates replacement nodes. Equal adjacent inorder values invalidate a strict BST.

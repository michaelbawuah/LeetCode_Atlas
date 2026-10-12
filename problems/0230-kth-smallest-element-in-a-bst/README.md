# 230 · Kth Smallest Element in a BST

[LeetCode problem](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## Intuition
Inorder traversal visits a BST's values in increasing order, so the kth visit is the required value.

## Baseline and approach
Collecting the entire inorder sequence costs O(n) time and storage. An explicit stack emits values incrementally and stops as soon as k visits have occurred. The input is a nonempty BST and k identifies an existing node.

## Why it works
The stack descends through each remaining left subtree before visiting its parent, then advances into the right subtree. This is inorder order, which is sorted for a BST. Decrementing k once per visit selects exactly the requested rank.

## Complexity
For height h and requested rank k: **O(h+k) time, O(h) auxiliary space**. The work includes paths pushed before the kth visit; stopping early avoids traversing every node when unnecessary.

## Pitfalls
Do not decrement k while pushing nodes: pushing is not visiting. This traversal depends on the BST ordering guarantee.

## Follow-up
Store subtree sizes to answer repeated kth-rank queries in O(h) time while supporting inserts and deletes.

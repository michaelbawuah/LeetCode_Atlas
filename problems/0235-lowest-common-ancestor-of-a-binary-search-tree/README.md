# 235 · Lowest Common Ancestor of a Binary Search Tree

[LeetCode problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Intuition
BST ordering tells whether both targets lie below one child or split at the current node.

## Baseline and approach
Recording both root paths takes O(h) storage. Follow the shared search region directly until its root lies between the two target values.

## Why it works
If both values are smaller, their common ancestors below the current node lie in the left subtree; the larger case is symmetric. The first node between them is either one target or their split point, so neither child subtree contains both. It is therefore the lowest common ancestor.

## Complexity
**O(h) time; O(1) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Return the original node, not a new node with the same value. Both distinct target references exist in a unique-valued BST. Input links and values remain unchanged.

## Follow-up
Compare the general-tree solution when ordering information is unavailable.

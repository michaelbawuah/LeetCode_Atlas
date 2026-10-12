# 106 · Construct Binary Tree from Inorder and Postorder Traversal

[LeetCode problem](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## Intuition
Reading postorder backward introduces root, right region, then left region.

## Baseline and approach
Recursive slicing can repeat linear copying at every level. The iterative version mirrors the preorder/inorder construction: read postorder backward and compare pending ancestors against inorder read from right to left.

## Why it works
The pending stack holds nodes whose reverse-inorder position has not yet been consumed. Until the top matches that position, the next reverse-postorder node extends its right subtree. Popping completed ancestors moves past their right regions; the next node begins the last completed ancestor's left subtree. Uniqueness fixes every boundary.

## Complexity
**O(n) time; O(h) auxiliary; O(n) output space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
The traversal directions are both reversed; combining forward inorder with backward postorder breaks the invariant. New nodes must not alias a previous call's result.

## Follow-up
Compare this construction with preorder/inorder reconstruction and identify the symmetric operations.

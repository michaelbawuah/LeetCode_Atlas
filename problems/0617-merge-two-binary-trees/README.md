# 617 · Merge Two Binary Trees

[LeetCode problem](https://leetcode.com/problems/merge-two-binary-trees/)

## Intuition
Corresponding positions sum their existing values; a position present in only one tree keeps that value.

## Baseline and approach
Recursive merging is concise but can overflow on a deep chain. Iterative paired traversal creates a fully independent output instead of returning borrowed input branches.

## Why it works
Each pending triple identifies one output position and the two corresponding input positions. Its value is their sum. Creating a child whenever either input child exists preserves exactly the union of positions; applying the same rule reaches every input node once.

## Complexity
**O(n + m) time; O(h1 + h2) auxiliary; O(n + m) fresh output space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
An unmatched subtree is copied, so changing the returned tree cannot change either input. Output allocation is part of the memory bound. Zero is only an arithmetic substitute for an absent position.

## Follow-up
Compare this fresh-output policy with an in-place merge that reuses branches and specify its aliasing contract.

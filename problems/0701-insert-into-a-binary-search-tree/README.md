# 701 · Insert into a Binary Search Tree

[LeetCode problem](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

## Intuition
Each comparison selects the only subtree whose value range can contain the new key.

## Baseline and approach
Rebuilding a BST from all values discards existing identities and costs O(n). Follow the search path to its first absent child and attach one new leaf.

## Why it works
The search maintains lower and upper bounds implied by its ancestors. Choosing left or right according to comparison preserves those bounds. At a missing child, the new value satisfies every ancestor constraint, so attaching it there preserves strict BST order.

## Complexity
**O(h + 1) time; O(1) auxiliary; one fresh node space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
The new value is absent under the contract. Return the original root for nonempty input and preserve every existing node and value. An empty input returns the fresh node.

## Follow-up
Add balancing rotations to prevent repeated ordered inserts from producing a long chain.

# 450 · Delete Node in a BST

[LeetCode problem](https://leetcode.com/problems/delete-node-in-a-bst/)

## Intuition
Replace the removed position with a subtree root that preserves its value bounds.

## Baseline and approach
Rebuilding from the remaining inorder values changes every node and takes O(n). Search the key, then reconnect its child or physically transplant its inorder successor.

## Why it works
A node with at most one child can be replaced by that child directly. With two children, the smallest right-subtree node is greater than the entire left subtree and no larger than other right values. Detaching it from its old parent and transplanting it preserves strict ordering and every remaining node.

## Complexity
**O(h) time; O(1) auxiliary; existing nodes reused space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Deleting the root changes the returned reference. A successor may have a right child that must be reattached. This implementation detaches the removed node and preserves all other node values and identities.

## Follow-up
Maintain subtree sizes during deletion to support rank queries afterward.

# 108 · Convert Sorted Array to Binary Search Tree

[LeetCode problem](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

## Intuition
Choosing a midpoint leaves subarrays whose sizes differ by at most one.

## Baseline and approach
Inserting sorted values one at a time creates a chain. Midpoint subdivision places a central key at each subtree root and builds its two ranges directly.

## Why it works
Every left-range value is smaller than its midpoint and every right-range value is larger, establishing strict BST ordering. The two range sizes differ by at most one, so recursively applying the same split bounds their heights and produces a balanced tree.

## Complexity
**O(n) time; O(log(n + 1)) auxiliary; O(n) output space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
There can be several correct balanced shapes. The semantic checker compares inorder values and balance rather than one chosen midpoint convention. Index ranges avoid copied slices.

## Follow-up
Build a balanced BST from a sorted linked list while avoiding repeated midpoint scans.

## C++23 implementation

C++23 uses the same half-open midpoint ranges. Every newly created node is staged in a `unique_ptr` until construction succeeds, giving exception-safe cleanup at the cost of O(n) ownership bookkeeping. Only then does the output transfer to the judge, or local `TreeResultOwner`; borrowed arena nodes are never owned this way. The adapter also verifies that the input array is unchanged.

C++23 submission cost: **O(n) time; O(n) ownership staging; O(log(n + 1)) traversal; O(n) output space**. Here n is node count, h is tree height, w is maximum level width, and L is the number of returned path elements when applicable. Adapter construction, snapshots, and serialization are measured separately.

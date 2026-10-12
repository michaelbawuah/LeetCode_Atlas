# 143 · Reorder List

[LeetCode problem](https://leetcode.com/problems/reorder-list/)

## Intuition
The desired order alternates the first remaining node with the last remaining node. Reversing the second half makes those final nodes available from a forward pointer.

## Baseline and approach
An array of node references makes alternating ends straightforward with O(n) space. This implementation finds the midpoint, disconnects the halves, reverses the second half, and weaves their nodes together. The first half has at least as many nodes as the second.

## Why it works
Splitting gives the original prefix and suffix. Reversing the suffix exposes its nodes in decreasing original-position order. Each weave consumes one node from each half, creating the next required pair. If the list length is odd, the extra first-half node remains as the final node.

## Complexity
For n nodes: **O(n) time, O(1) auxiliary space**. No new list nodes are created.

## Pitfalls
Disconnect the halves before reversing, or the result can contain a cycle. Save both next pointers before rewiring. The LeetCode method changes the list in place and returns `None`; local metadata tells the adapter to serialize argument zero after the call.

## Follow-up
Can the same split-and-weave idea be generalized to alternate nodes from three equal-length segments?

## C++23 implementation

C++23 has the standard `void reorderList(ListNode*)` interface. After split, reversal, and weaving, the adapter serializes argument zero and verifies the exact original-node order, unchanged values, and termination without extra nodes or a cycle. No new list nodes are created.

C++23 submission cost: **O(n) time; O(1) space**. Here n is node count, h is tree height, w is maximum level width, and L is the number of returned path elements when applicable. Adapter construction, snapshots, and serialization are measured separately.

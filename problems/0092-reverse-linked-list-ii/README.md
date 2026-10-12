# 92 · Reverse Linked List II

[LeetCode problem](https://leetcode.com/problems/reverse-linked-list-ii/)

## Intuition
Grow the reversed segment by repeatedly moving its next node to the segment's front.

## Baseline and approach
Collecting the list and rebuilding a selected slice uses O(n) extra space. After reaching the segment's predecessor, the pointer solution repeatedly extracts the node after its original first node and inserts it immediately after that predecessor.

## Why it works
The predecessor remains fixed, and `first` remains the tail of the reversed portion. Each extraction moves the next original node to the front, extending the reversed portion by one while preserving the untouched suffix. Exactly `right-left` extractions reverse the intended inclusive segment.

## Complexity
**O(n) time; O(1) space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Positions are one-based. The original first node stays the segment tail throughout; advancing it would corrupt the loop invariant. A dummy head covers a reversal beginning at position one.

## Follow-up
How would you reverse several disjoint ranges while limiting repeated traversal?

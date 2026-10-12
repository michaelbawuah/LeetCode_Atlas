# 404 · Sum of Left Leaves

[LeetCode problem](https://leetcode.com/problems/sum-of-left-leaves/)

## Intuition
A leaf contributes only when its incoming edge is a left edge.

## Baseline and approach
A full parent map could identify leaf directions but stores unnecessary references. Carry one incoming-direction flag with each DFS entry.

## Why it works
The flag records exactly whether the current node was reached through its parent's left child. The contribution condition also checks both missing children, selecting all and only left leaves once.

## Complexity
**O(n) time; O(h) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
A left child with descendants is not a leaf. The root has no incoming left edge and does not contribute as a singleton.

## Follow-up
Return separate sums of left and right leaves in one traversal.

## Python and C++23
Both versions carry the incoming direction and count only qualifying leaves. The official node/value bounds keep the accumulated sum within int in C++; neither traversal mutates borrowed nodes.

C++23 submission-method complexity: **O(n) time; O(h) space**. Adapter ownership and JSON conversion are separate.

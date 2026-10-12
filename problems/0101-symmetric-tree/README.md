# 101 · Symmetric Tree

[LeetCode problem](https://leetcode.com/problems/symmetric-tree/)

## Intuition
Matching mirror positions compare opposite child directions.

## Baseline and approach
A traversal with explicit null positions can be reversed for comparison. Pairwise mirror traversal checks the same structural condition without storing a full encoding.

## Why it works
The initial pair contains the root children. Equal-valued pairs schedule outside children together and inside children together. Those are exactly the next mirror positions; any missing-node mismatch witnesses asymmetry. Exhausting all pairs establishes matching shape and values.

## Complexity
**O(n) time; O(h) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Equal level values alone do not establish mirrored shape. Null positions must match across opposite child directions.

## Follow-up
Return the first mismatched mirror positions as a diagnostic witness.

## Python and C++23
Both versions compare opposite child positions through explicit pairs, retaining borrowed input links and values unchanged. Mirrored shapes with different node values are rejected.

C++23 submission-method complexity: **O(n) time; O(h) space**. Adapter ownership and JSON conversion are separate.

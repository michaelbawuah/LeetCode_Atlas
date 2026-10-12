# 61 · Rotate List

[LeetCode problem](https://leetcode.com/problems/rotate-list/)

## Intuition
Only the remainder of k after whole-list cycles changes the order.

## Baseline and approach
Repeated one-position rotations can take O(nk). Find the length and new tail once, connect the old tail to the old head, and cut at the new tail.

## Why it works
A right shift of r moves the final r nodes before the preceding n-r nodes. The located new tail ends that prefix. Joining the original ends preserves their cyclic order, and cutting after the new tail produces precisely the required linear sequence.

## Complexity
**O(n) time; O(1) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Reduce k modulo length before walking. Empty lists avoid division by zero. Break the temporary cycle before returning.

## Follow-up
Rotate several times while maintaining a persistent circular representation and a separate visible head.

## Python and C++23
Both versions locate the new tail after reducing k modulo length, temporarily connect the old ends, then cut the cycle. Every output node is borrowed from the original list and remains arena-owned.

C++23 submission-method complexity: **O(n) time; O(1) space**. Adapter ownership and JSON conversion are separate.

# 86 · Partition List

[LeetCode problem](https://leetcode.com/problems/partition-list/)

## Intuition
Build two stable streams, then join the smaller-valued stream before the other.

## Baseline and approach
Copying node references into two arrays uses O(n) memory. Two dummy-headed chains retain the same original order with constant pointer state.

## Why it works
Each processed node joins exactly one chain at its tail. Appending in encounter order preserves relative order within each partition. Clearing the old next link prevents the chains from retaining edges into unprocessed nodes; the final concatenation satisfies the threshold ordering.

## Complexity
**O(n) time; O(1) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Values equal to x belong to the second chain. Save the old next pointer before detaching. Stability is part of the answer, so sorting would change the contract.

## Follow-up
Partition into three stable ranges around two thresholds using the same tail-based technique.

## Python and C++23
Both implementations form two stable chains of borrowed nodes and concatenate them. Clearing each incoming node next-link avoids stale connections or cycles. Dummy nodes have local lifetime and never appear in output.

C++23 submission-method complexity: **O(n) time; O(1) space**. Adapter ownership and JSON conversion are separate.

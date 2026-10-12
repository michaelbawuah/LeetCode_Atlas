# 83 · Remove Duplicates from Sorted List

[LeetCode problem](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

## Intuition
Keep the first node of each sorted run and bypass its later copies.

## Baseline and approach
A set could remember seen values, but sorted adjacency supplies the same information without extra storage.

## Why it works
The current node is the retained representative of its run. Bypassing an equal successor leaves that representative in place; moving forward after a different value starts the next run. Exactly one original node survives per distinct value.

## Complexity
**O(n) time; O(1) space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
After bypassing an equal successor, stay on the current node because more duplicates can follow. This version keeps one occurrence; List II removes all repeated values.

## Follow-up
How would removal change when equal values are not adjacent?

## Python and C++23
Both versions retain the first node of each equal-valued run and bypass later copies. Borrowed nodes are never explicitly deleted, so arena ownership remains valid after links change.

C++23 submission-method complexity: **O(n) time; O(1) space**. Adapter ownership and JSON conversion are separate.

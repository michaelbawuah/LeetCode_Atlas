# 2 · Add Two Numbers

[LeetCode problem](https://leetcode.com/problems/add-two-numbers/)

## Intuition
Carry state lets the next output digit depend only on the current input digits.

## Baseline and approach
For input lengths m and n, converting both lists into integers is a useful test oracle, but digitwise arithmetic keeps the submission independent of whole-number conversion.

## Why it works
Before each iteration, emitted digits match the low-order sum and carry is the remaining overflow into the next position. Division by ten produces the next carry and remainder digit. A final carry creates its own output node.

## Complexity
**O(max(m, n)) time; O(1) auxiliary; O(max(m, n)) fresh output space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Inputs use least-significant digits first. Do not lose the final carry or alter either input. The returned list consists of fresh nodes.

## Follow-up
Add numbers represented most-significant digit first without reversing the input lists.

## Python and C++23
Python retains only carry/tail state besides new output nodes. C++ stages every fresh node in unique_ptr storage so construction exceptions free all partial output; after success the local runner immediately owns the returned list through ListResultOwner. Neither implementation changes or aliases input nodes. Borrowed input nodes remain ListArena-owned.

C++23 submission-method complexity: **O(max(m, n)) time; O(max(m, n)) auxiliary ownership staging; O(max(m, n)) fresh output space**. Adapter ownership and JSON conversion are separate.

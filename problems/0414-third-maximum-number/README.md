# 414 · Third Maximum Number

[Problem](https://leetcode.com/problems/third-maximum-number/) · Easy

## Idea and approaches

Maintain the three largest distinct values while reading the stream. Sorting distinct values is an O(n log n) baseline; only three slots are needed.

## Correctness invariant

After each value, the occupied slots are the largest up to three distinct values of the processed prefix in descending order. Existing values change nothing; inserting a new value in its ordered position and shifting smaller slots preserves that invariant. The third slot is the answer if filled, otherwise the first slot is the maximum.

## Complexity

O(n) time and O(1) auxiliary space. Input is preserved, and None markers are distinct from every legal integer.

## Verification and pitfalls

Tests compare against a distinct full sort, covering repeated maxima, negative values, and the minimum signed value.

The request is the third distinct maximum, not the third item after sorting with duplicates. A legal minimum integer cannot serve as an unused-slot sentinel.

**Follow-up:** How would a bounded min-heap track the kth distinct maximum?

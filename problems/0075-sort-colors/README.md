# 75 · Sort Colors

[Problem](https://leetcode.com/problems/sort-colors/) · Medium

## Idea and approaches

Partition the array into zero, one, unknown, and two regions. General sorting is an O(n log n) baseline; the Dutch national flag scan classifies each unknown entry in linear time.

## Correctness invariant

Before each step, entries before low are zero, low through scan - 1 are one, and entries after high are two. Swapping a zero to low extends the first two regions; swapping a two to high reduces the unknown region but brings an unexamined value to scan. A one simply extends the middle region. When no unknown values remain, the array is sorted.

## Complexity

O(n) time and O(1) auxiliary space. Both implementations mutate the original array and return no value.

## Verification and pitfalls

Properties compare with an independent full sort and check list identity. Fixtures cover all equal values, already ordered input, and zeroes swapped in from the right.

Do not advance scan after moving a two to the end: its replacement still needs classification.

**Follow-up:** How would partitioning change with four colors or an arbitrary pivot?

## Python and C++23

C++ uses signed scan boundaries and vector references; all exchanges mutate the same vector. Both versions have constant auxiliary space and no copied input parameters. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.

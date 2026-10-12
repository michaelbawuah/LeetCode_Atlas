# 167 · Two Sum II — Input Array Is Sorted

[Problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · Medium · Two pointers

## Idea

Sorted order lets the current sum tell us which endpoint cannot be part of an answer.

**Baseline:** enumerate every pair in O(n²) time. Binary-searching a partner for
each value improves that to O(n log n).
**Chosen approach:** start at both ends. A sum below target moves the left pointer
rightward; a sum above target moves the right pointer leftward.

## Why it works

If the current sum is too small, pairing the current left value with any remaining
right value can only decrease the sum, so that left value can be discarded.
If the sum is too large, pairing the current right value with any remaining left
value can only increase it, so that right value can be discarded. These safe
steps preserve the guaranteed pair until it is found.

## Complexity

O(n) time and O(1) auxiliary space. Each step reduces the remaining interval by one.
The input is already sorted; the solution does not sort or copy it.

## Tests and pitfalls

Fixtures cover equal values, negative numbers, middle pairs, and zeroes. Generated
tests enumerate all index pairs and retain the problem's unique-answer condition.
The returned indices are **one-based**. Keep `left < right` so an element is
never paired with itself.

**Follow-up:** what extra storage would be useful if the input were unsorted?

# 704. Binary Search

[Problem on LeetCode](https://leetcode.com/problems/binary-search/) · Easy

## Intuition
Sorted order lets one comparison discard half of the remaining candidates.

## Approaches
- **Baseline:** scan every element: O(n) time and O(1) space.
- **Optimized:** search an inclusive interval and remove the middle element after every unsuccessful comparison.

## Correctness invariant
If the target exists and has not been returned, its index lies inside `[left, right]`. A middle value smaller than the target rules out every index at or to its left; a larger one rules out every index at or to its right. Each update preserves the invariant and strictly shortens the interval. An empty interval therefore proves absence.

## Complexity
O(log n) time and O(1) extra space. The input is not copied or changed.

## Edge cases and pitfalls
Use `left <= right` for inclusive bounds and move past the middle on either update. Test one-element arrays and both endpoints. The input contract is sorted, strictly increasing values.

## Follow-up
Find the first position where the target could be inserted, then adapt the search to first and last occurrences when duplicates are allowed.

## Verification
Named local cases and an independent generated-input oracle accompany this solution. No official judge result is recorded.

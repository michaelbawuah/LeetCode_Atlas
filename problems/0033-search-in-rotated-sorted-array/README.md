# 33. Search in Rotated Sorted Array

[Problem on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) · Medium

## Intuition
Rotation creates one discontinuity. At least one half of any candidate interval remains sorted; use that half's endpoints to decide whether it can contain the target.

## Approaches
- **Baseline:** scan the rotated array: O(n) time and O(1) space.
- **Optimized:** identify the sorted half at each middle and retain only the half that can contain the target.

## Correctness invariant
If the target exists and has not been returned, its index is inside `[left, right]`. With distinct values, `nums[left] <= nums[middle]` identifies a sorted left half; otherwise the right half is sorted. Membership in the sorted half's value range determines which half can safely be discarded. Every iteration halves the remaining candidate interval.

## Complexity
O(log n) time and O(1) extra space. No separate pivot scan or copied slices are needed.

## Edge cases and pitfalls
The array may be unrotated or contain one or two elements. Include the sorted half's outer endpoint and exclude the already-checked middle. Distinct values are essential: duplicates can make the sorted-half test ambiguous.

## Follow-up
Handle duplicate values. Explain why the worst-case complexity can become linear even with a binary-search-style loop.

## Verification
Named local cases and an independent generated-input oracle accompany this solution. No official judge result is recorded.

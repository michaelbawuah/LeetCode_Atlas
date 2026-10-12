# 88 · Merge Sorted Array

[Problem](https://leetcode.com/problems/merge-sorted-array/) · Easy

## Idea and approaches

Merge from the largest remaining values into the spare slots at the end of nums1. A baseline combines and sorts both logical inputs, requiring O((m + n) log(m + n)) time and copied storage.

## Correctness invariant

The filled suffix is the correctly merged suffix of all consumed elements. Selecting the larger last unconsumed element extends it by one. Writing backward cannot destroy a still-needed first-array element. When nums2 is exhausted, the untouched nums1 prefix is already correctly positioned.

## Complexity

O(m + n) time and O(1) auxiliary space. Mutate nums1 and preserve nums2. Only the first m entries of nums1 are original data; its remaining entries are capacity placeholders.

## Verification and pitfalls

Tests compare against sorting the two original logical inputs, check None return and identity, and verify nums2 remains unchanged. Empty logical inputs and genuine zero values are covered.

Placeholders may be zero even when zero is real data; lengths m and n decide which values belong to the input.

**Follow-up:** Why does a forward in-place merge risk overwriting values that have not been consumed?

## Python and C++23

Both C++ vectors are received by reference. Only nums1 is written; nums2 is preserved. The runner returns the changed vector to match the mutation-aware Python adapter. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.

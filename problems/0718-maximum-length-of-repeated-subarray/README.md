# 718 · Maximum Length of Repeated Subarray

[LeetCode problem](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)

## Intuition
Equal newest elements extend a matching contiguous suffix by one; a mismatch resets it.

## Baseline and approach
Enumerating slices and testing membership is the baseline. A rolling row stores the longest matching suffix for each endpoint pair.

## Why it works
An equal pair can follow only the previous row’s previous column, so its suffix length is that diagonal plus one. Unequal endpoints share no nonempty matching suffix. Scanning columns downward preserves the old diagonal while the maximum records the best suffix anywhere.

## Complexity
Python: **O(m n) time; O(min(m, n)) auxiliary space**. m and n are array lengths. Reference swapping selects the shorter row; O(mn) work uses O(min(m,n)) storage and preserves both inputs.

## Pitfalls
This is a contiguous subarray, unlike LCS. Do not retain the top or left optimum across mismatches. Duplicate values are allowed.

## Follow-up
How would rolling hashes and a length binary search change the running time?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

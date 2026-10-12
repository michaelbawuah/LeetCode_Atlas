# 424. Longest Repeating Character Replacement

[Problem on LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/) · Medium

## Intuition
Within a window, keep its most frequent letter and replace every other letter. The required number of replacements is `window length - highest frequency`.

## Approaches
- **Baseline:** enumerate substrings while counting their letters: O(n²) time for a fixed alphabet, O(1) extra space.
- **Optimized:** maintain a window and 26 counts. Shrink from the left until its exact replacement cost is at most k.

## Correctness invariant
The counts exactly describe the current window. Once the shrink loop ends, that window is feasible. Extending a window cannot reduce its replacement cost, so a left boundary already discarded as infeasible cannot become useful at a later right endpoint. The algorithm therefore checks the longest feasible suffix for each endpoint and retains the largest length.

## Complexity
O(n) time because each boundary moves at most n times and scanning 26 counts is constant work. O(1) extra space for a 26-entry array. More generally, recomputing the maximum costs O(a) per boundary movement for alphabet size a.

## Edge cases and pitfalls
k may be zero or cover the entire string. A one-letter string is always feasible. This implementation recomputes the actual maximum after shrinking; mixing an exact-maximum proof with a stale maximum is misleading.

## Follow-up
Allow different replacement costs for different letters. Does the same frequency-based feasibility test still work?

## Verification
Named local cases and an independent generated-input oracle accompany this solution. No official judge result is recorded.

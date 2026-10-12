# 516 · Longest Palindromic Subsequence

[LeetCode problem](https://leetcode.com/problems/longest-palindromic-subsequence/)

## Intuition
Equal endpoints can surround a smaller palindromic subsequence; unequal endpoints require dropping one.

## Baseline and approach
Enumerating subsequences is exponential. Interval DP computes the best length while rolling away the left-endpoint dimension.

## Why it works
Before each right endpoint is updated, best[right] is the interval without the new left character, best[right−1] is the current interval without the right character, and diagonal is the old inner interval. Equal endpoints extend the inner optimum by two; otherwise the best omitted-endpoint case is optimal.

## Complexity
Python: **O(n²) time; O(n) auxiliary space**. n is length. Both implementations use O(n²) time and O(n) row states. C++ receives a string reference, and neither version copies candidate subsequences.

## Pitfalls
A subsequence may have gaps. Save the old diagonal before overwrite. A singleton has length one and an empty inner interval length zero.

## Follow-up
How would the state change when at most one mismatched pair is allowed?

## C++23 counterpart
**O(n²) time; O(n) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

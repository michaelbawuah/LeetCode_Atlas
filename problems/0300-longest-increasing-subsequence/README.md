# 300 · Longest Increasing Subsequence

[LeetCode problem](https://leetcode.com/problems/longest-increasing-subsequence/)

## Intuition
A smaller ending value is more useful for extending a subsequence of the same length. Keep the smallest possible tail for each length.

## Baseline and approach
Enumerating subsequences is exponential; comparing each position with all predecessors gives an O(n²) DP. Binary searching the ordered tail values reduces processing to O(n log n).

## Why it works
After each prefix, tails[k] is the minimum final value attainable by an increasing subsequence of length k+1. Replacing the first tail at least as large as a new value preserves existing lengths while improving their future extension options. Appending establishes a new longer subsequence. Thus the tail count equals the optimum length.

## Complexity
For n numbers: **O(n log n) time, O(n) auxiliary space**.

## Pitfalls
Use bisect_left for strictly increasing sequences: equal values replace rather than extend. The final tails array represents best endpoints and need not itself be a subsequence of the input.

## Follow-up
How would predecessor indices let you return an actual longest increasing subsequence?

## Python and C++23 comparison

Python's `bisect_left` and C++'s `std::lower_bound` both find the first tail at least as large as the new value. This implements strict increase: equal values replace a tail rather than extending the length. Both take O(n log(n + 1)) time and O(n) auxiliary space, with scalar output. C++ reserves a tails vector for n integers up front, avoiding later growth allocations without changing the asymptotic space bound. Neither input is modified, and neither tails collection by itself reconstructs an actual subsequence.

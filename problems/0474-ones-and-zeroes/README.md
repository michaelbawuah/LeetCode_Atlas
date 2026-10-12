# 474 · Ones and Zeroes

[LeetCode problem](https://leetcode.com/problems/ones-and-zeroes/)

## Intuition
Each string consumes two resources: its zero count and one count.

## Baseline and approach
Enumerating every subset is exponential. A two-resource 0/1 knapsack stores the largest selectable count at each budget pair.

## Why it works
For each string, a budget state either excludes it or adds it to a predecessor with both required resources removed. Descending traversal prevents using the same array position again in that iteration, even when one resource cost is zero. Thus every table state is optimal for the processed strings.

## Complexity
Python: **O(T + W(m + 1)(n + 1)) time; O((m + 1)(n + 1)) auxiliary space**. W is string count and T their total characters; m and n are resource budgets. Counting characters costs O(T), then O(W(m+1)(n+1)) work uses a table of O((m+1)(n+1)) entries.

## Pitfalls
Duplicate string values remain separate available positions. A string containing only zeros or only ones still consumes the other budget by zero. Current official m and n are both at least one.

## Follow-up
How would differing values per string change the objective?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

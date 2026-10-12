# 91 · Decode Ways

[LeetCode problem](https://leetcode.com/problems/decode-ways/)

## Intuition
A valid grouping ends in a one-digit token from 1 to 9 or a two-digit token from 10 to 26. Count both possibilities when available.

## Baseline and approach
Enumerating every possible token grouping is exponential. A prefix DP caches those overlapping counts; only the previous two prefix lengths are needed.

## Why it works
Before reading the next digit, one_back counts decodings of the previous prefix and two_back counts decodings of the prefix before that. A nonzero single digit extends the former; a valid two-digit token extends the latter. These alternatives end with different token lengths, so their counts add without duplication.

## Complexity
For n digits: **O(n) time, O(1) auxiliary space**.

## Pitfalls
Zero is never a valid single-digit token. A pair beginning with zero is invalid, while 10 and 20 are valid. Inputs are nonempty digit strings; fixtures include leading and internal zeros.

## Follow-up
What extra cases are needed if a wildcard can represent any digit from 1 through 9?

# 8. String to Integer (atoi)

[Problem on LeetCode](https://leetcode.com/problems/string-to-integer-atoi/) · Medium

## Approach

A regular expression can capture the numeric prefix but allocates a match/string. Scan spaces, one optional sign, and decimal digits with scalar state.

## Invariant and correctness

The accumulated value is exactly the numeric prefix consumed after the sign. The first nondigit ends that prefix. Further digits cannot bring an already overflowing magnitude back into range, so early clamping is safe.

## Complexity

Time: O(n). Space: O(1).

## Boundaries and pitfalls

Skip ASCII spaces only; do not search for a later number or accept two signs. An empty digit prefix represents zero.

## Follow-up

Return both the parsed integer and the first unconsumed character index.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

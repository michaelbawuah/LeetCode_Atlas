# 115 · Distinct Subsequences

[LeetCode problem](https://leetcode.com/problems/distinct-subsequences/)

## Intuition
For each source character, either ignore it or use it as the next matching target character. Count selections of source positions, not distinct resulting string values.

## Baseline and approach
Enumerating all target-length index combinations is exponential. A one-dimensional DP stores counts for each target prefix and updates from longest to shortest.

## Why it works
Before a source character is processed, counts[j] counts selections from the previous source prefix producing the first j target characters. A match adds counts[j−1] for selections using the newest position. Descending updates ensure that this character is used at most once. counts[0] is one because the empty selection is unique.

## Complexity
For source length m and target length n, **O(mn) arithmetic operations and O(n) integer states**. Python integers avoid overflow; their bit widths and arithmetic costs can grow for intermediate states even though the final answer is guaranteed to fit a signed 32-bit integer.

## Pitfalls
Ascending updates can reuse the same source character. Repeated source letters create different selections even when the produced target text is identical. Both strings are nonempty and matching is case sensitive.

## Follow-up
How would you count only selections whose chosen source positions are at most a fixed distance apart?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.

## C++23 counterpart

Every count update uses only nonnegative addition and copying. Clamping each count to INT_MAX commutes with these operations: min(M, min(M, a) + min(M, b)) = min(M, a + b). Each sum is widened to int64_t before addition and then clamped. The guaranteed final answer fits int, so its clamped value remains exact even when unrelated intermediate counts exceed 64 bits. Descending column updates preserve use of each source position at most once. The regression uses 1000 source a characters and a target of 500 a characters followed by b: target-prefix counts become huge while the final count remains zero. By-value strings add O(m + n) bytes, and the core holds O(n + 1) fixed-width states.

C++: **O(m n + m + n) time; O(m + n) including string copies; O(n + 1) DP states space**. Named fixtures and 150 reproducible generated inputs compare this implementation with the Python track.

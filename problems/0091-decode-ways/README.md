# 91 · Decode Ways

[LeetCode problem](https://leetcode.com/problems/decode-ways/)

## Intuition
A valid grouping ends in a one-digit token from 1 to 9 or a two-digit token from 10 to 26. Count both possibilities when available.

## Baseline and approach
Enumerating every possible token grouping is exponential. A prefix DP caches those overlapping counts; only the previous two prefix lengths are needed.

## Why it works
Before reading the next digit, one_back counts decodings of the previous prefix and two_back counts decodings of the prefix before that. A nonzero single digit extends the former; a valid two-digit token extends the latter. These alternatives end with different token lengths, so their counts add without duplication.

## Complexity
Python, for n digits: **O(n) arithmetic operations and O(1) integer states**. Only the final answer is bounded; arbitrary-precision prefix counts can grow to O(n) bits before a later invalid token eliminates all decodings. This bound counts arithmetic operations, rather than their bit cost.

## Pitfalls
Zero is never a valid single-digit token. A pair beginning with zero is invalid, while 10 and 20 are valid. Inputs are nonempty digit strings; fixtures include leading and internal zeros.

## Follow-up
What extra cases are needed if a wildcard can represent any digit from 1 through 9?

## C++23 counterpart

Every count update uses only nonnegative addition and copying. Clamping each count to INT_MAX commutes with these operations: min(M, min(M, a) + min(M, b)) = min(M, a + b). Each sum is widened to int64_t before addition and then clamped. The guaranteed final answer fits int, so its clamped value remains exact even when unrelated intermediate counts exceed 64 bits. Here zero or invalid-pair transitions select a stored count or zero; clamping commutes with that selection too. A 100-digit regression has huge counts for its first 98 ones and then an invalid final double zero, so its answer is zero. The by-value input string occupies O(n) bytes; the recurrence itself holds two fixed-width counts.

C++: **O(n) time; O(n) including string copy; O(1) core auxiliary space**. Named fixtures and 150 reproducible generated inputs compare this implementation with the Python track.

# 494 · Target Sum

[LeetCode problem](https://leetcode.com/problems/target-sum/)

## Intuition
Track how many partial sign assignments reach each subtotal. Each next value creates both a plus and a minus branch.

## Baseline and approach
Enumerating all 2^n sign choices is the baseline. A frequency map merges assignments that reach the same subtotal while retaining their multiplicities.

## Why it works
Before processing a value, each map entry counts exactly the assignments to earlier positions yielding that key. Every assignment has two distinct choices for the next sign, so adding its count to both successor subtotals covers all assignments once. If the value is zero, both successors share a key but represent distinct expressions and both counts must be added.

## Complexity
For n values with total S, **O(n(S+1)) expected time and O(S+1) auxiliary space**. The extra one covers all-zero arrays. Dictionary operations have expected constant lookup cost; official n ≤ 20 bounds the count by 2^20.

## Pitfalls
Negative targets are valid. Zero doubles the number of assignments. Using a set of reachable totals would lose multiplicity.

## Follow-up
How can the nonnegative input values convert this into a subset-sum counting problem?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.

## C++23 counterpart

The sparse frequency map preserves both sign choices even when a value is zero. Map lookup is expected constant time. For n <= 20 there are at most 2^20 sign assignments; official sum S <= 1000 bounds subtotal keys, so int arithmetic is safe for keys and multiplicities. The input vector is read by reference, and the following map replaces the previous layer without copying it.

C++: **O(n (S + 1)) expected time; O(S + 1) space**. Named fixtures and 150 reproducible generated inputs compare this implementation with the Python track.

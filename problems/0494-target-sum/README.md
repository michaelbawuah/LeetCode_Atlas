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

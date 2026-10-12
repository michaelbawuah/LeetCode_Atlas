# 338 · Counting Bits

[LeetCode problem](https://leetcode.com/problems/counting-bits/)

## Intuition
Removing the lowest bit leaves the count for a smaller number. Add one only when that removed bit was set.

## Baseline and approach
Counting each number’s binary digits separately repeats work and costs O(n log n). Reuse counts[value >> 1] to compute each next entry in constant time.

## Why it works
When processing value, its right-shifted predecessor is smaller and its count has already been computed. Right shift removes exactly the least significant bit, so the predecessor count plus value & 1 gives the complete count. The zero entry establishes the base case.

## Complexity
For upper bound n: **O(n) time, O(n) storage including the returned list; O(1) space beyond the output**.

## Pitfalls
The result includes both zero and n, so its length is n+1. Powers of two have one set bit. Keep the parentheses around value & 1 when combining bitwise and arithmetic operations.

## Follow-up
Can you derive the alternative recurrence using value & (value−1)?

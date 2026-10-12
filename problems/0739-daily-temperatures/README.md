# 739. Daily Temperatures

[Problem on LeetCode](https://leetcode.com/problems/daily-temperatures/) · Medium

## Intuition
Days that have not yet found a warmer future day can wait on a stack. A new warmer temperature resolves the most recent cooler days first.

## Approaches
- **Baseline:** scan forward from each day until a warmer temperature appears: O(n²) time, O(1) auxiliary space besides the output.
- **Optimized:** maintain indexes of unresolved days in nonincreasing temperature order.

## Correctness invariant
Every index on the stack has no warmer day in the processed suffix after it. When today's temperature exceeds the top's temperature, today is that index's first warmer day: earlier days failed to resolve it. Pop and record the distance until the remaining top is at least as warm. Unresolved indexes at the end correctly retain zero.

## Complexity
O(n) time because each index is pushed once and popped at most once. O(n) extra stack space and O(n) output space.

## Edge cases and pitfalls
Equal temperatures do not count as warmer. Descending and flat inputs leave zero answers. Store indexes rather than only temperatures so distances can be computed.

## Follow-up
How would you answer the same question if the days formed a circular sequence?

## Verification
Named local cases and an independent generated-input oracle accompany this solution. No official judge result is recorded.

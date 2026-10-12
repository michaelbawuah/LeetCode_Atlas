# 155. Min Stack

[Problem on LeetCode](https://leetcode.com/problems/min-stack/) · Medium

## Intuition
Each stack entry can remember the minimum of everything at or below it. Removing the top then exposes the correct earlier minimum automatically.

## Approaches
- **Baseline:** store values and scan them for `getMin`: O(n) for that query, O(1) amortized push/pop, O(n) space.
- **Optimized:** store `(value, prefix minimum)` pairs. Every operation uses the last pair.

## Correctness invariant
For every entry i, its stored minimum equals the minimum of values from the bottom through i. Pushing takes the smaller of the new value and the previous prefix minimum. Popping leaves every remaining prefix unchanged. Thus the top pair answers both `top` and `getMin` correctly.

## Complexity
O(1) amortized time for push and pop with Python lists, O(1) worst-case for top and getMin, and O(n) extra space for n current values. The LeetCode operation model describes these as constant-time stack operations.

## Edge cases and pitfalls
Repeated minimum values must survive one of their copies being popped. Negative values and 32-bit limits require no special arithmetic. `pop`, `top`, and `getMin` are only called on a nonempty stack under the problem contract.

## Follow-up
Support `getMax` as well, or design a queue that supports a minimum query using two such stacks.

## Verification
Named local cases and an independent generated-input oracle accompany this solution. No official judge result is recorded.

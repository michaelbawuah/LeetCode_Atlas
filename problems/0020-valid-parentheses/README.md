# 20. Valid Parentheses

[Problem on LeetCode](https://leetcode.com/problems/valid-parentheses/) · Easy

## Intuition
A closing bracket must match the most recently opened bracket that has not yet closed. That is exactly a stack's last-in, first-out rule.

## Approaches
- **Baseline:** repeatedly erase adjacent matching pairs until no change: O(n²) worst-case time, O(n) space for strings.
- **Optimized:** push openings; for a closing bracket, require a matching stack top and pop it.

## Correctness invariant
The stack contains exactly the unmatched opening brackets from the processed prefix, in their opening order. Each closer must close its top element; a different type or an empty stack proves invalidity immediately. After the final character, an empty stack means every opening had a correctly nested matching close.

## Complexity
O(n) time and O(n) extra space in the worst case, such as a string containing only opening brackets.

## Edge cases and pitfalls
A closing bracket can arrive before any opening. Equal counts of each type are insufficient: `([)]` has matching counts but invalid nesting. Remember to check for leftover openings.

## Follow-up
If strings may contain arbitrary text, how should brackets inside quoted strings and escaped characters be handled?

## Verification
Named local cases and an independent generated-input oracle accompany this solution. No official judge result is recorded.

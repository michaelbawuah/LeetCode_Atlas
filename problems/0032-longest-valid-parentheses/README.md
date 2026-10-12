# 32 · Longest Valid Parentheses

[LeetCode problem](https://leetcode.com/problems/longest-valid-parentheses/)

## Intuition
Keep indices of unmatched opening parentheses above the most recent invalid boundary.

## Baseline and approach
Enumerating every substring and checking its balance costs O(n²). An index stack identifies the longest valid suffix ending at each character in one pass.

## Why it works
After a matched closing parenthesis removes one opening index, the stack top is the boundary just before the longest valid suffix ending here. If popping empties the stack, this closing character cannot be matched and becomes the next boundary. Every valid substring ends at a closing character, so the maximum suffix length is sufficient.

## Complexity
Python: **O(n) time; O(n) auxiliary space**. n is string length. Each index is pushed and popped at most once. Python and C++ keep O(n) indices and do not copy or modify the input string.

## Pitfalls
An empty string is valid input. Seed the stack with −1, and restore a boundary after an unmatched closing character; do not confuse unmatched opens with invalid closes.

## Follow-up
Can two directional scans recover the same maximum with constant auxiliary space?

## C++23 counterpart
**O(n) time; O(n) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

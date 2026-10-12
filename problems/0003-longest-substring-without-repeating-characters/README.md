# 3. Longest Substring Without Repeating Characters

[Problem on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · Medium

## Intuition
A repeated character tells us exactly how far the left edge must move. Remember its latest index instead of rescanning the window.

## Approaches
- **Baseline:** start at every index and extend until a duplicate: O(n²) time in the worst case, O(min(n, a)) space.
- **Optimized:** track each character's latest index and jump the left boundary beyond duplicates that are inside the current window.

## Correctness invariant
After processing each right endpoint, `s[left:right + 1]` has no duplicates and is the longest valid suffix ending there. A repeated character forces the left edge past its previous occurrence; `max` prevents an occurrence outside the window from moving that edge backward. Every candidate substring ends somewhere, so the maximum of these suffix lengths is the answer.

## Complexity
O(n) expected time with dictionary operations; O(min(n, a)) extra space for the latest indexes, where a is the number of possible input characters.

## Edge cases and pitfalls
The empty string returns zero. Spaces and punctuation count as characters. Using `left = last_seen[char] + 1` without `max` fails on `abba`.

## Follow-up
Adapt the window to allow at most k distinct characters. What information replaces each character's latest index?

## Verification
Named local cases and an independent generated-input oracle accompany this solution. No official judge result is recorded.

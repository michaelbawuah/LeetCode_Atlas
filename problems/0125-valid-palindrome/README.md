# 125 · Valid Palindrome

[Problem](https://leetcode.com/problems/valid-palindrome/) · Easy · Two pointers

## Idea

Compare meaningful characters from opposite ends, skipping punctuation and spaces.
Lowercase the two characters being compared to ignore case.

**Baseline:** construct the normalized string and compare it with its reverse:
O(n) time and O(n) auxiliary space.
**Chosen approach:** two pointers examine the original string with O(1) extra space.
For `"1,2,1"`, the commas are skipped and the matching digits remain.

## Why it works

At each step, all retained characters outside the pointer interval already form
matching pairs. Skipping a non-alphanumeric character does not alter the normalized
sequence. A mismatch disproves a palindrome; a match shrinks the remaining interval.
When the pointers meet or cross, every required pair has matched.

## Complexity

O(n) time and O(1) auxiliary space. Every pointer moves inward at most n times.
The problem uses printable ASCII, so character classification and lowercasing
are constant-size operations.

## Tests and pitfalls

Cover punctuation-only text, case changes, digits, spaces, and an ordinary mismatch.
The independent oracle filters using an ASCII regular expression and compares a
reversed copy. A second property generates mirrored alphanumeric text around punctuation.
Digits count as meaningful characters; `"0P"` is not a palindrome.

**Follow-up:** what normalization rules would be needed for user-visible Unicode text?

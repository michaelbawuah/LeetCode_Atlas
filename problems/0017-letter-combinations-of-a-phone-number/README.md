# 17. Letter Combinations of a Phone Number

[Problem on LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) · Medium

## Approach, invariant, and complexity

Each digit contributes one independent choice of letters. Their Cartesian product enumerates each possible combination exactly once.

A baseline recursive builder and the itertools product both visit the necessary outputs. The product keeps one choice position for each digit; every emitted tuple chooses exactly one valid letter per digit, and every possible tuple occurs once.

For d digits, there are at most 4^d combinations and joining each costs O(d), giving O(d × 4^d) time and output space. Product state needs O(d) auxiliary space under the fixed four-letter bound.

An empty input returns an empty list rather than a list containing the empty string. Digits are restricted to 2 through 9. Returned ordering is not significant.

Follow-up: generate combinations lazily, or prune them against a dictionary prefix trie.

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

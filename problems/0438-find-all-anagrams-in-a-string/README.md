# 438. Find All Anagrams in a String

[Problem on LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/) · Medium

## Approach

Sorting each candidate window takes O(nm log m). Maintain exact letter counts for a fixed-width window and compare 26 counters.

## Invariant and correctness

The window counters describe the last min(m, processed length) characters. Once width reaches m, equal counters mean exactly the same multiset of letters, so the recorded start is an anagram.

## Complexity

Time: O(n + m) for the fixed alphabet. Space: O(1) auxiliary; O(n) output.

## Boundaries and pitfalls

Multiplicity matters, and overlapping matches must remain. The fixed lowercase alphabet makes counter comparison constant work.

## Follow-up

Track only how many counters differ to support a much larger alphabet.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

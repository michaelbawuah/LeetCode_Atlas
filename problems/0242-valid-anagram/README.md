# 242 · Valid Anagram

[Problem](https://leetcode.com/problems/valid-anagram/) · Easy · Frequency counting

## Idea

An anagram changes order while preserving the number of occurrences of every
character. A set alone loses the multiplicities that matter.

**Baseline:** sort both strings and compare: O(n log n + m log m) time.
**Chosen approach:** reject unequal lengths, then compare two `Counter` objects.
For `"aacc"` and `"ccac"`, the character sets match but the counts do not.

## Why it works

Each counter records the exact multiplicity of each character. Equal counters
mean every occurrence can be paired with one of the same character in the other
string, so a rearrangement exists. A different count makes such pairing impossible.

## Complexity

O(n + m) expected time and O(σ) auxiliary space, where σ is the number of distinct
characters encountered. With the problem's lowercase English alphabet, σ ≤ 26,
so auxiliary space is O(1). Unequal lengths return immediately.

## Tests and pitfalls

Tests include different lengths, a one-character mismatch, and equal character
sets with unequal frequencies. Generated tests use sorting as an independent
oracle and check reversal and added-character transformations.

`Counter` also handles Unicode code points, but user-visible Unicode equivalence
may require an explicit normalization policy.

**Follow-up:** how would you compare anagrams when strings arrive as streams?

# 131 · Palindrome Partitioning

[LeetCode problem](https://leetcode.com/problems/palindrome-partitioning/)

## Intuition
Precompute which intervals are palindromes, then choose a sequence of palindromic intervals that covers the string.

## Baseline and approach
Enumerating all cut masks and reversing every piece is the baseline. An O(n²) palindrome table makes each subsequent interval-validity lookup constant time.

## Why it works
The interval table is correct because equal endpoints around a shorter palindrome form a palindrome; intervals of length one or two supply the base cases. Backtracking maintains a palindromic partition of the consumed prefix. Trying every valid next endpoint includes every complete partition once.

## Complexity
For length n and K partitions, **O(n²+n2^n) time and O(n²) auxiliary space**, including the table and recursion. Output occupies **O(Kn)** space. Substring copies along the current path contain at most n total characters.

## Pitfalls
The outer answer order is free; the order of pieces within each partition is fixed. Sorting inner rows would merge different partitions or accept reordered pieces. An entire palindrome and its finer cuts may all be valid answers.

## Follow-up
How would you compute the minimum number of cuts without enumerating all partitions?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.

## C++23 counterpart

C++ uses the same palindrome-interval table and endpoint search. Substring and output copies are charged by character count; the live path covers at most n characters. The checker reorders only complete partitions, preserving the order of pieces within each partition.

Time: O(n^2 + n 2^n). Space: O(n^2) auxiliary; O(K n) output.

The JSON adapter creates fresh state per case. Named fixtures and 150 deterministic generated inputs compare the two language implementations; existing independent Python oracles supply a separate behavioral reference.

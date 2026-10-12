# 205. Isomorphic Strings

[Problem on LeetCode](https://leetcode.com/problems/isomorphic-strings/) · Easy

## Approach

Pairwise comparison of equality relationships takes O(n²). Maintain mappings in both directions while scanning corresponding characters.

## Invariant and correctness

Both maps describe a bijection for the processed prefix. A conflicting forward or reverse association invalidates that bijection; adding a consistent pair preserves it.

## Complexity

Time: O(n) expected. Space: O(a), a is encountered alphabet size.

## Boundaries and pitfalls

A forward map alone permits several source characters to share one target. Input lengths are equal. The C++ fixed table uses the official ASCII domain.

## Follow-up

Return the mapping itself or group many strings by a canonical equality signature.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

C++ uses two fixed 256-entry tables with unsigned-char indexes for the official ASCII domain. Python uses dictionaries; C++ has deterministic linear time and constant table storage.

Time: O(n). Space: O(1), two fixed ASCII tables.

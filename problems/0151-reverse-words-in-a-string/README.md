# 151. Reverse Words in a String

[Problem on LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/) · Medium

## Approach

A manual token parser can scan boundaries explicitly. split discards repeated whitespace and reversed supplies tokens in reverse order before joining with one space.

## Invariant and correctness

Tokens are exactly the input words in order. Reversing them preserves each word internally and changes only their ordering; joining canonicalizes separators.

## Complexity

Time: O(n). Space: O(n) including output.

## Boundaries and pitfalls

The official input uses ASCII spaces and contains a word. Python split also handles other whitespace, while the C++ counterpart targets the official domain.

## Follow-up

Perform the transformation in a mutable character buffer with constant auxiliary space.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

C++ tokenizes a copied string stream, stores words, and appends them in reverse order. Stream, word, and output copies are included in O(n) memory.

Time: O(n) amortized. Space: O(n) including output and stream/token copies.

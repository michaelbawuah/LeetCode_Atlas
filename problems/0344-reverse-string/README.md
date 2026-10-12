# 344. Reverse String

[Problem on LeetCode](https://leetcode.com/problems/reverse-string/) · Easy

## Approach

A reversed copy uses O(n) extra space. Swap corresponding endpoints inside the supplied list.

## Invariant and correctness

After each swap the processed prefix and suffix contain their final reversed characters. The unprocessed interval shrinks until every pair has been placed.

## Complexity

Time: O(n). Space: O(1).

## Boundaries and pitfalls

Return None and mutate the existing list. C++ submission code uses vector<char>; its adapter translates JSON one-character strings explicitly.

## Follow-up

Reverse words within the same buffer while preserving their internal character order.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

Both implementations mutate the supplied character container with constant auxiliary storage and return void/None. The C++ adapter owns a vector<char> decoded from JSON one-character strings and serializes those strings after reversal.

Time: O(n). Space: O(1).

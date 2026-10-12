# 7. Reverse Integer

[Problem on LeetCode](https://leetcode.com/problems/reverse-integer/) · Medium

## Approach

A string conversion can reverse the digits with O(number of digits) storage. Extract decimal digits into a scalar instead.

## Invariant and correctness

After each iteration result is the reversal of the digits already removed, and remaining contains the unprocessed prefix. Restoring the original sign gives the reversed integer; reject a result outside signed 32-bit range.

## Complexity

Time: O(log(|x| + 1)). Space: O(1).

## Boundaries and pitfalls

Python bounds the magnitude before appending each digit. A C++ counterpart must check multiplication/addition before overflowing, and must not take abs of INT_MIN in an int.

## Follow-up

Reverse digits in a supplied base while keeping a fixed signed-width result.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

C++ uses int throughout and checks decimal multiplication/addition against numeric_limits<int> before executing it. Signed remainder/division avoid taking abs(INT_MIN). Python also checks the permitted magnitude before each decimal append.

Time: O(log(|x| + 1)). Space: O(1).

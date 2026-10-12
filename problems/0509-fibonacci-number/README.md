# 509. Fibonacci Number

[Problem on LeetCode](https://leetcode.com/problems/fibonacci-number/) · Easy

## Approach, invariant, and complexity

Keep only the previous two Fibonacci values. The recurrence never needs older entries.

A baseline recursive expansion repeats subproblems exponentially; a full table takes O(n) space. Before iteration i, the two scalars are F(i) and F(i + 1). Advancing with their sum preserves the invariant, so n iterations return F(n).

Time is O(n), and auxiliary space O(1) under the bounded n ≤ 30 contract. n = 0 needs no iteration.

Update both states using their old values, rather than overwriting one before computing the other.

Follow-up: compute F(n) for very large n using fast doubling and modular arithmetic.

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp)

Both implementations keep two scalars. C++ int values, including the intermediate next Fibonacci value, fit under n ≤ 30.

Time: O(n). Space: O(1). The local adapter constructs a fresh object for each fixture and owns any converted inputs.

# 179 · Largest Number

[Problem](https://leetcode.com/problems/largest-number/) · Medium

## Idea and approaches

Order two number strings by whether a+b or b+a is lexicographically larger. Numerical or ordinary lexicographic sorting is a tempting baseline but does not optimize concatenation.

## Correctness invariant

For equal total length, a larger concatenated digit string denotes a larger number. If two neighboring strings are in the wrong concatenation order, swapping them improves the complete result without changing the surrounding prefix and suffix. Sorting by the concatenation comparison removes these improving swaps and yields a maximal ordering; equal comparisons permit either order.

## Complexity

For n values with at most d digits each, time is O(n log n * d), including comparisons, and auxiliary/output storage is O(nd). Here d is bounded by the numeric domain.

## Verification and pitfalls

The independent oracle enumerates all permutations of small inputs and compares complete concatenations. Prefix pairs such as 121 and 12, and all-zero inputs, are named cases.

Normalize an all-zero result to one zero. Comparing number values alone gives the wrong ordering for 10 and 2.

**Follow-up:** How would you explain why the concatenation comparator is transitive using repeating digit strings?

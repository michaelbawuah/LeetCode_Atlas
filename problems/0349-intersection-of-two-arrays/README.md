# 349 · Intersection of Two Arrays

[Problem](https://leetcode.com/problems/intersection-of-two-arrays/) · Easy

## Idea and approaches

Intersect the two sets of values, ignoring multiplicity. Pairwise membership comparisons are an O(nm) baseline; hashing supports expected linear work.

## Correctness invariant

A value belongs in the answer exactly when it appears in both arrays. Converting each input to a set removes repeated evidence without changing membership; set intersection therefore returns exactly the required unique values.

## Complexity

Python uses O(n + m) expected time and O(n + m) auxiliary storage, plus at most O(min(n, m)) output. Neither input is modified.

## Verification and pitfalls

The oracle enumerates the small legal value domain and checks ordinary list membership. It separately rejects duplicate output values. Fixtures include repeated inputs, no intersection, zero, and value limits.

An unordered checker permits different output orders but still preserves duplicate multiplicity when comparing results.

**Follow-up:** Which two-pointer approach is useful if the arrays are already sorted?

## Python and C++23

C++ stores only nums1 values in a hash set and erases each matched value when emitted, taking O(n) auxiliary storage rather than constructing two input sets. Time remains O(n + m) expected, output is O(min(n, m)), and both referenced inputs are preserved. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.

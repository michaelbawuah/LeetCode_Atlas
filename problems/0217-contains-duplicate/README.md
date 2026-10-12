# 217 · Contains Duplicate

[Problem](https://leetcode.com/problems/contains-duplicate/) · Easy · Hash set

## Idea

A duplicate exists as soon as a value has appeared earlier.

**Baseline:** compare every pair: O(n²) time, O(1) space. Sorting would reduce
time to O(n log n), but would either change the input or require a copy.
**Chosen approach:** scan into a set and stop at the first repeat.

## Why it works

Before processing an element, `seen` contains exactly the distinct values in
the processed prefix. Membership proves a duplicate; absence permits extending
that prefix without introducing one. Reaching the end proves all values differ.

## Complexity

O(n) expected time and O(n) auxiliary space. An early repeat can stop the scan
sooner. The time bound assumes expected constant-time set operations.

## Tests and pitfalls

Test singleton, all-distinct, adjacent repeats, negative values, and repeats far
apart. The property oracle compares pairs directly. A second property starts
with distinct values and appends one existing value.

Values, rather than indices, belong in the set. Avoid sorting the caller's array
unless mutation is an intentional part of the interface.

**Follow-up:** what changes if you must report all duplicated values or work
under a strict memory limit?

## Python and C++23

Both versions use a hash set, taking O(n) expected time and O(n) auxiliary space. C++ reserves capacity and tests whether insertion succeeds; Python checks membership before adding. C++ receives the vector by reference and neither version mutates it. Hash-table operations have expected, rather than guaranteed worst-case, constant time.

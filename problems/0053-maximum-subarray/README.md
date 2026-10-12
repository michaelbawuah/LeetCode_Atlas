# 53 · Maximum Subarray

[Problem](https://leetcode.com/problems/maximum-subarray/) · Medium · Kadane's algorithm

## Idea

A best subarray ending at the current position either starts here or extends
the best subarray ending one position earlier.

**Baseline:** enumerate every nonempty slice and sum it, costing O(n³) with
repeated summation. Rolling sums per starting position reduce this to O(n²).
**Chosen approach:** use `ending_here = max(value, ending_here + value)` and
remember the largest value of that state.

## Why it works

Inductively, `ending_here` is the largest sum among nonempty subarrays ending at
the previous position. Any subarray ending at the new position is either the
singleton or a previous ending subarray extended by the new value. Choosing
between those two possibilities maintains the invariant. The best answer over
all ending positions covers every nonempty subarray.

## Complexity

Python: O(n) time and O(1) auxiliary space. Iteration uses indices rather than a
slice, avoiding an extra copied list.

## Tests and pitfalls

Test all-negative arrays, a singleton zero, a losing prefix, and a worthwhile
negative bridge. Generated tests enumerate all nonempty slices. Initializing the
best value to zero would incorrectly allow an empty answer on all-negative input;
initialize from the first value instead.

**Follow-up:** which extra state lets you return the winning start and end indices?

## Python and C++23 comparison

Both versions use the same two scalar Kadane states, so time is O(n) and auxiliary space is O(1); neither changes the input. Python integers grow as needed. C++ widens running sums to `long long` before addition, then returns `int`: the official constraints keep the maximum sum within that return type. Initializing from the first element preserves the requirement that the chosen subarray be nonempty.

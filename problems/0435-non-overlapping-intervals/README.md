# 435 · Non-overlapping Intervals

[Problem](https://leetcode.com/problems/non-overlapping-intervals/) · Medium · Greedy scheduling

## Idea

Minimizing removals is equivalent to keeping the largest compatible subset.
An interval that finishes earlier leaves more room for every later choice.

**Baseline:** try all subsets and retain the largest non-overlapping one,
requiring exponential time.
**Chosen approach:** sort by end, then greedily keep each interval whose start
is at least the last kept end. Return the number not kept.

## Why it works

Among intervals compatible with the already chosen prefix, consider the earliest
finisher. Replacing the next interval of any optimal schedule with that finisher
cannot invalidate the later intervals, because its end is no later. An optimal
schedule therefore exists that makes the greedy choice. Applying the same exchange
argument to the remaining intervals proves maximality of the kept subset.

## Complexity

O(n log n) time and O(n) auxiliary space for Python's sorted copy and workspace.
The scan itself uses constant space and leaves input intervals unchanged.

## Tests and pitfalls

Include identical, nested, negative, and equal-end intervals. The property oracle
enumerates compatible subsets. Touching endpoints are **compatible** here,
so use `start >= previous_end`. Sorting by start and always keeping the first
interval fails on `[[1, 10], [2, 3], [3, 4]]`.

**Follow-up:** why does adding weights to intervals require a different strategy?

# 128 · Longest Consecutive Sequence

[Problem](https://leetcode.com/problems/longest-consecutive-sequence/) · Medium · Hash set

## Idea

A consecutive run has exactly one value whose predecessor is absent. Start a
walk only at those values, so the same run is never traversed from each member.

**Baseline:** sort the numbers, skip duplicates, and scan consecutive runs:
O(n log n) time.
**Chosen approach:** build a set, find run starts, and walk each run using membership.
For `[100, 4, 200, 1, 3, 2]`, only `1` starts the four-value run.

## Why it works

Every finite consecutive run has a smallest value and that value's predecessor
is absent. The outer loop therefore starts a walk for every run. Each walk
continues exactly while successors exist and counts the whole run. Other members
are skipped as starts. The maximum length is consequently the required answer.

## Complexity

Python: O(n) expected time and O(n) auxiliary space. Although the loops are nested,
each unique value participates in at most one successor walk. Hash operations
are expected constant time. Empty input returns zero.

## Tests and pitfalls

Cases cover negative runs, duplicates, separated extremes, and empty input.
The oracle uses sorting; translation and duplicating the input preserve the answer.
Iterate over the set rather than the original list: repeated copies of a run's
start could otherwise cause repeated walks.

**Follow-up:** how would you update the answer after each newly inserted number?

## Python and C++23 comparison

Both implementations build a hash set and start successor walks only where a predecessor is absent. Expected time is O(n), auxiliary space O(n), and scalar output space O(1); neither modifies the input. C++ uses `unordered_set`, whose lookup cost can be linear in the worst case, so expected linear time is not a worst-case guarantee. It explicitly guards `INT_MIN` predecessor subtraction and `INT_MAX` successor addition to avoid signed overflow; Python does not have fixed-width integer overflow.

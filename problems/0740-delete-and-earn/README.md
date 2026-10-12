# 740 · Delete and Earn

[LeetCode problem](https://leetcode.com/problems/delete-and-earn/)

## Intuition
Combine equal values into one earned amount, then choose nonadjacent value groups.

## Baseline and approach
Enumerating compatible value subsets is exponential. Sorting distinct values turns the task into a rolling take-or-skip recurrence.

## Why it works
Taking a value collects all its occurrences because they do not conflict with one another. Consecutive groups conflict, so the new optimum either skips the group or adds its earnings to the state before its neighbor. A numerical gap creates no conflict and permits adding the earnings to the current best.

## Complexity
Python: **O(n + U log U) expected time; O(U) auxiliary space**. n is item count and U the number of distinct values. Both versions use expected O(n+U log U) time and O(U) frequency/sorted storage. C++ widens value×frequency before multiplication; inputs are preserved.

## Pitfalls
Adjacency is by value, not input position. A gap between sorted distinct values must not be treated as a conflict. Do not allocate a dense table up to an unbounded maximum value unnecessarily.

## Follow-up
How would deleting values within distance two change the predecessor state?

## C++23 counterpart
**O(n + U log U) expected time; O(U) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

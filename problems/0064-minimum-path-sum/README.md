# 64 · Minimum Path Sum

[LeetCode problem](https://leetcode.com/problems/minimum-path-sum/)

## Intuition
A cheapest route to a cell ends with the cheaper of its top and left predecessors.

## Baseline and approach
Enumerating full routes repeats subproblems. A rolling DP row keeps each predecessor’s optimum instead.

## Why it works
The old value at a column describes the route from above, while the updated previous column describes the route from the left. Adding the current cell’s cost to their minimum gives the optimum for this cell. The first column has only a predecessor from above, establishing the boundary.

## Complexity
Python: **O(r c) time; O(c) auxiliary space**. r and c are dimensions. Row storage is O(c), inputs are preserved, and C++ stores path sums in int64_t before returning the bounded int answer.

## Pitfalls
Include both endpoint costs. Updating from right to left would mix rows incorrectly. The Python infinity entries are only initial sentinels: all returned route costs are integers.

## Follow-up
How would parent directions allow reconstruction of a cheapest route?

## C++23 counterpart
**O(r c) time; O(c) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

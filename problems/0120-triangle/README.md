# 120 · Triangle

[LeetCode problem](https://leetcode.com/problems/triangle/)

## Intuition
A cheapest path from one triangle cell continues through one of its two adjacent children.

## Baseline and approach
Enumerating root-to-bottom choices is exponential. Compute suffix costs from the bottom upward, reusing one row.

## Why it works
Before updating a row, best[column] and best[column+1] describe optimal costs from the two child positions. Their minimum plus the current value is the correct suffix optimum. Left-to-right updates keep the second child’s old value available until used.

## Complexity
Python: **O(h²) time; O(h) auxiliary space**. h is triangle height. Both versions use O(h²) time and O(h) row storage. The copied bottom row is included in that space; C++ widens sums to int64_t.

## Pitfalls
Negative values are legal, so a locally smallest next value is insufficient. Copy the bottom row to preserve the triangle.

## Follow-up
How would you return the sequence of triangle positions in an optimal path?

## C++23 counterpart
**O(h²) time; O(h) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

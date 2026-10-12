# 221 · Maximal Square

[LeetCode problem](https://leetcode.com/problems/maximal-square/)

## Intuition
An all-one square ending here extends the smallest square at its top, left, and top-left neighbors.

## Baseline and approach
Checking every candidate square by scanning its cells is the baseline. A rolling side-length DP avoids repeated scans.

## Why it works
For a one cell, all three neighboring squares must support an extension, so one plus their minimum is the largest feasible side. A zero cell supports side zero. Keeping the previous diagonal before overwrite preserves the previous-row dependency. The maximum side squared is the required area.

## Complexity
Python: **O(r c) time; O(c) auxiliary space**. r and c are dimensions. Both solutions use O(c) row states and preserve the matrix. The C++ adapter converts JSON character strings into vector<vector<char>> before the method runs.

## Pitfalls
Matrix entries are character strings, not integers. Return area rather than side length. Clear the state when a zero interrupts a square.

## Follow-up
How can a histogram method find the largest rectangle instead?

## C++23 counterpart
**O(r c) time; O(c) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

# 213 · House Robber II

[LeetCode problem](https://leetcode.com/problems/house-robber-ii/)

## Intuition
The circular edge makes the first and last houses incompatible. Solve two lines: one without the last house and one without the first.

## Baseline and approach
Enumerating circular independent subsets is exponential. Each of the two linear subproblems uses the rolling take-or-skip recurrence from House Robber.

## Why it works
Every valid selection excludes at least one endpoint when there are two or more houses. Therefore it belongs to at least one linear subproblem. Each line computes its own optimal nonadjacent selection; the larger optimum is exactly the circular optimum. A singleton is handled separately because its value should remain selectable.

## Complexity
For n houses: **O(n) time, O(1) auxiliary space**. Index ranges avoid temporary slices.

## Pitfalls
Running the linear algorithm on the entire circle can select both endpoints. Excluding both endpoints unnecessarily can miss the optimum. Handle one house before splitting the ranges.

## Follow-up
What changes when the forbidden neighbor distance is two rather than one?

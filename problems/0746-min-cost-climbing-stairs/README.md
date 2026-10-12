# 746 · Min Cost Climbing Stairs

[LeetCode problem](https://leetcode.com/problems/min-cost-climbing-stairs/)

## Intuition
The destination is just beyond the last listed stair. Reaching it means paying for the stair used to make the final jump.

## Baseline and approach
A recursive search tries every route starting at stair zero or one. Instead, compute the cheapest cost to reach each position, retaining only the previous two positions.

## Why it works
Before computing position i, the states hold minimum costs to reach i−2 and i−1. A final jump from either predecessor pays that predecessor’s cost. Taking the minimum covers every possible final jump. Positions zero and one both start with zero cost because either can be chosen directly.

## Complexity
For n costs: **O(n) time, O(1) auxiliary space**.

## Pitfalls
The cost belongs to the stair being departed, not the destination. The top has no listed cost. Choosing the cheapest individual stair greedily can force costly later jumps.

## Follow-up
How would you reconstruct a cheapest route, and what extra storage would that require?

# 198 · House Robber

[LeetCode problem](https://leetcode.com/problems/house-robber/)

## Intuition
At each house, either skip it and keep the previous best, or take it and add its amount to the best ending before its neighbor.

## Baseline and approach
Enumerating nonadjacent subsets is exponential. A DP table uses `best[i] = max(best[i-1], best[i-2] + nums[i])`. Since only the last two entries matter, retain them in two variables instead of an array.

## Why it works
Before processing a house, `one_back` is optimal for all prior houses and `two_back` is optimal for all prior houses except the immediate neighbor. Every valid choice either skips this house or takes it while excluding that neighbor. Taking the maximum covers both possibilities, and shifting the two states preserves their meaning.

## Complexity
For n houses: **O(n) time, O(1) auxiliary space**.

## Pitfalls
Update the states together so the new value cannot overwrite the older value needed by the recurrence. A greedy choice of the locally largest house can block a better combination of its neighbors.

## Follow-up
When the first and last houses are adjacent, compare two linear subproblems that exclude one of those endpoints.

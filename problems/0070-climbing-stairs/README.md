# 70 · Climbing Stairs

[LeetCode problem](https://leetcode.com/problems/climbing-stairs/)

## Intuition
A complete route reaches the last stair by a one-step jump or a two-step jump. Count those two disjoint groups.

## Baseline and approach
Enumerating every step sequence grows exponentially. Tabulating the number of routes for each height is linear; storing only the previous two counts removes the table.

## Why it works
Before advancing to height i, the two states count routes ending at heights i−2 and i−1. Every route to i ends with one of the two allowed jumps, so adding those counts includes each route exactly once. The initial counts for heights zero and one are both one.

## Complexity
For n stairs: **O(n) time, O(1) auxiliary space**.

## Pitfalls
The zero-height count is one because doing nothing is one completed route. Update both rolling states together. The fixtures stay within the positive-height problem domain, including n = 45.

## Follow-up
How does the state change if jumps of one, two, or three stairs are allowed?

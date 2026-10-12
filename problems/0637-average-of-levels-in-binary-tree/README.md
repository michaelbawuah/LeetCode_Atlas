# 637 · Average of Levels in Binary Tree

[LeetCode problem](https://leetcode.com/problems/average-of-levels-in-binary-tree/)

## Intuition
A queue round supplies both the sum and count for one level.

## Baseline and approach
Storing complete level rows before averaging uses O(n) temporary values. Accumulate a sum while consuming each fixed-size frontier.

## Why it works
At the round start, count is exactly the number of nodes at the current depth. Summing those popped values and dividing by count therefore gives that level mean. Enqueued children belong exclusively to the following round.

## Complexity
**O(n) time; O(w) auxiliary; O(h) output space.** Here n counts nodes, h is height, and w is maximum actual level width when relevant. Special symbols are explained in the approach. Adapter construction and serialization are separate.

## Pitfalls
Capture count before adding children. Compare numerical outputs with a tolerance; integer input values can have fractional means.

## Follow-up
Compute weighted level averages when every node has a separate positive weight.

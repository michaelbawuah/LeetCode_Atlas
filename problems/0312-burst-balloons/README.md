# 312 · Burst Balloons

[LeetCode problem](https://leetcode.com/problems/burst-balloons/)

## Intuition
Choose the last balloon burst inside an interval, so its outer neighbors remain fixed.

## Baseline and approach
Enumerating removal orders is factorial. Interval DP fixes the final removal and combines two smaller independent intervals.

## Why it works
If last is the final balloon in [left,right], all other interior balloons are already gone and its neighbors are the two interval boundaries. The left and right regions were burst independently, and their optimal scores plus this final product cover every legal last choice. Increasing interval length ensures both subproblems are available.

## Complexity
Python: **O(n³) time; O(n²) auxiliary space**. n is balloon count. The padded copy uses O(n) space and the interval table O(n²). O(n³) transition work dominates. The original list is preserved.

## Pitfalls
Choosing the first balloon does not leave independent regions because neighbors change. Keep boundary value one at both ends, and distinguish original indices from the padded array.

## Follow-up
How would you reconstruct one optimal burst order?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

# 112 · Path Sum

[LeetCode problem](https://leetcode.com/problems/path-sum/)

## Intuition
Carry the sum for each root-to-current-node path, then test it only at leaves.

## Baseline and approach
Enumerating every path into a separate array stores more than a yes/no query needs. The DFS frontier retains only each node and its current sum, returning as soon as a matching complete path appears.

## Why it works
Each child receives its parent's exact path sum plus its own value. Thus every visited sum corresponds to the unique root path for that node. Accepting only at a leaf witnesses a complete matching path, and exhausting the frontier examines all possible endpoints.

## Complexity
**O(n) time; O(h) space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Matching an internal prefix is insufficient. Negative values prevent pruning solely because the current total exceeds the target. An empty tree has no complete path.

## Follow-up
Return every matching path while retaining one mutable path rather than copying each partial path.

## Python and C++23
Both versions carry a root-path sum through an explicit DFS stack and leave tree links unchanged. C++ uses long long for intermediate sums. TreeArena owns the borrowed input nodes.

C++23 submission-method complexity: **O(n) time; O(h) space**. Adapter ownership and JSON conversion costs are separate.

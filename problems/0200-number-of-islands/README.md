# 200 · Number of Islands

[LeetCode problem](https://leetcode.com/problems/number-of-islands/)

## Intuition
Each unseen land cell starts one component. Flood-fill its connected land so no later cell counts that component again.

## Baseline and approach
A separate visited set supports a straightforward traversal. This solution stores the visited mark directly in the grid by replacing reached `"1"` cells with `"0"`. An explicit stack explores the four orthogonal neighbors without recursive call-depth risk. The input is a nonempty rectangular grid as required by the problem.

## Why it works
A flood-fill follows exactly the permitted land edges, so it marks all and only the land in the starting cell's island. Marking before pushing prevents duplicate work. The outer scan starts a new fill only on land not reached by an earlier fill; therefore it increments once per island.

## Complexity
For rows × cols cells: **O(rows × cols) time, O(rows × cols) worst-case auxiliary space** for the stack. Each cell is scanned, and each land cell is pushed at most once. The input grid is modified.

## Pitfalls
Diagonal contact does not connect islands. Mark on discovery, not after popping, to avoid duplicate stack entries. Copy the grid first when the caller needs to preserve it.

## Follow-up
Use disjoint sets to support adding one land cell at a time and reporting the evolving component count.

## Python and C++23 comparison

Both sources mark discovered land directly in the supplied grid and traverse iteratively. C++ receives `vector<vector<char>>`; the runner owns the decoded char matrix and reads each JSON cell as a one-character string. The scalar island count is returned, while the runner’s private grid is modified. O(rows × cols) time and worst-case stack space exclude the runner’s O(rows × cols) input copy. All traversal storage uses standard containers.

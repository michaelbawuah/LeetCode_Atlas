# 130 · Surrounded Regions

[Problem](https://leetcode.com/problems/surrounded-regions/) · Medium

## Idea

An open cell survives exactly when its open component reaches a border. Start from border cells, mark every connected open cell temporarily, then capture only the unmarked open cells.

**Baseline:** independently test each open cell's escape path, repeating traversal of shared components. One multi-source traversal shares that work.

## Why it works

The temporary marker identifies precisely cells reachable from an original border O through horizontal or vertical O neighbors. Those components cannot be surrounded. Every remaining O belongs to a component disconnected from all borders and must be captured. Restoring protected cells after traversal produces the requested board.

## Complexity

O(rows × cols) time and worst-case O(rows × cols) stack space. The method mutates the input board and returns None; local metadata reads the final board from argument 0. No separate output board is allocated by the solution.

## Counterexample and checks

Diagonal contact with a border O is not an escape route. Cases cover diagonal separation, thin boards, and a long open path to a border. The independent oracle searches outward from each original O rather than inward from all borders.

**Follow-up:** compute the number and total area of captured components during the same operation.

## Python and C++23 comparison

Both sources protect border-connected open cells using an explicit traversal stack and then capture the remaining open cells. C++ changes the supplied `vector<vector<char>>` in place and returns `void`, matching Python’s mutation contract. The runner decodes one-character JSON strings into chars and serializes the final board as one-character strings, avoiding numeric character codes. O(rows × cols) time and worst-case auxiliary stack space exclude the runner’s O(rows × cols) decoded input and serialized output copies. No recursion or manual allocation is used.

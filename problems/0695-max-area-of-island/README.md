# 695 · Max Area of Island

[Problem](https://leetcode.com/problems/max-area-of-island/) · Medium

## Idea

Flood-fill each unseen land component and count its cells. Mark a cell as water when it is pushed, then track the largest component area encountered.

**Baseline:** search from every land cell independently, repeatedly measuring the same islands. One marking traversal shares this work across the whole grid.

## Why it works

Each traversal starts at unseen land and follows exactly horizontal or vertical land edges. Every cell reachable from the start is eventually visited; every visited cell is connected to the start. Marking on insertion prevents duplicate pushes, so area counts each member exactly once. The outer scan starts one traversal per original island, and the maximum of their areas is the answer.

## Complexity

O(rows × cols) time and O(rows × cols) worst-case stack space. The solution changes land cells from 1 to 0. Local adapters copy fixtures before evaluation.

## Counterexample and checks

Diagonal land cells belong to different islands. Marking only after popping can also enqueue a shared neighbor twice and inflate its area. Named cases include diagonal components and a ring with several paths to its cells. The independent generated oracle merges adjacent land cells with union-find and measures component sizes.

**Follow-up:** return both the largest island's area and its perimeter without a second full traversal.

## Python and C++23 comparison

Both versions count components with an explicit coordinate stack and mark land as zero when pushed. Each cell is pushed at most once. Time is O(rows×cols), worst-case auxiliary stack storage O(rows×cols), and output one integer. Both mutate the supplied grid; each local adapter creates an independent grid from the JSON fixture before calling the solution.

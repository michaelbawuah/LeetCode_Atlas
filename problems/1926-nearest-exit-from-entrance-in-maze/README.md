# 1926 · Nearest Exit from Entrance in Maze

[Problem](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) · Medium

## Idea and approach

BFS open neighboring cells and stop at the first boundary cell other than the entrance.

**Baseline:** Solve all-pairs shortest paths among open maze cells and inspect each exit.

## Why it works

Every move costs one, so queue layers give shortest distances. The entrance is marked before expansion and can never be returned as a new boundary neighbor. Any newly reached boundary cell is a legal exit at minimum distance.

## Complexity

O(R C) time. O(R C) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

An entrance located on the border is excluded from the exit set; a 1×1 open maze has no exit. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Return all nearest exits without exploring deeper distance layers.

## Python and C++23 comparison

C++ takes the canonical vector of character rows; the JSON runner translates one-character strings into chars. The submitted solution itself uses a byte visited matrix and an O(R C) BFS queue, without mutating maze or entrance.

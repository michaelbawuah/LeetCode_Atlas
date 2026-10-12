# 909 · Snakes and Ladders

[Problem](https://leetcode.com/problems/snakes-and-ladders/) · Medium

## Idea and approach

Convert rolled-to labels using alternating row direction, follow at most one snake or ladder, and BFS over the resulting positions.

**Baseline:** Build every roll-transition edge and solve all-pairs shortest paths.

## Why it works

Every edge represents one dice roll followed by its mandatory single jump. BFS minimizes rolls, not the number of squares crossed. Marking the resulting destination avoids revisiting equivalent game states.

## Complexity

O(n^2) time. O(n^2) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

A ladder landing on another ladder does not cause a second jump in the same roll. Both the boustrophedon coordinates and the one-jump rule affect edges. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Use a weighted shortest-path model when dice outcomes have different costs.

## Python and C++23 comparison

C++ indexes numbered squares through integer division/remainder and reverses alternate row columns. Its visited vector marks resulting positions after a single board jump. O(n²) time and space; the board is not mutated.

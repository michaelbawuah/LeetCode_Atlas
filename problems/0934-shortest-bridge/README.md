# 934 · Shortest Bridge

[Problem](https://leetcode.com/problems/shortest-bridge/) · Medium

## Idea and approach

Find one complete island, then expand from all of its cells through water until the other island is reached.

**Baseline:** Label the two islands and compare every cross-island pair by Manhattan separation.

## Why it works

The initial frontier has zero flipped cells. Each water expansion adds one flip, and BFS processes those counts increasingly. First contact with the second island therefore yields the fewest water cells needed; its land cell does not add a flip.

## Complexity

O(n^2) time. O(n^2) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Starting from one arbitrary island cell can overestimate the bridge when another coast is nearer. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Return the water-cell coordinates of one minimum bridge.

## Python and C++23 comparison

Both sources first mark an entire island, then launch BFS from every one of its cells. C++ owns a seen matrix, island-discovery stack, and BFS queue and leaves the supplied grid unchanged. A BFS layer counts water cells already crossed; entering the second island does not add a flip. O(n²) time and auxiliary storage exclude the runner’s O(n²) decoded input copy. All graph traversal is iterative.

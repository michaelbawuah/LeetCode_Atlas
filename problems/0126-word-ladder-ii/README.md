# 126 · Word Ladder II

[Problem](https://leetcode.com/problems/word-ladder-ii/) · Hard

## Idea and approach

BFS records every predecessor that reaches a word at its minimum distance, then backtracking walks only these decreasing-distance edges.

**Baseline:** Enumerate all simple word chains and keep the shortest; this has factorial branching.

## Why it works

During a BFS layer, newly discovered words have the next minimum distance. Equal-distance discoveries add alternate predecessors; completing the layer retains every shortest route to the target. Every recovery edge decreases distance by one, so recovered chains are exactly the shortest ones. N is word count, L word length, E stored predecessor links, D shortest chain length, and P output chains.

## Complexity

O(N L^2 + P D) expected time. O(N L + E + D) auxiliary; O(P D) output word references space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Stopping immediately at the first target discovery loses other parents from the same layer. Source-to-target order inside each path remains significant. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Return shortest chains lazily while keeping the predecessor graph.

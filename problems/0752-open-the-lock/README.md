# 752 · Open the Lock

[Problem](https://leetcode.com/problems/open-the-lock/) · Medium

## Idea and approach

Run BFS on four-wheel states, with one modular increment or decrement per edge.

**Baseline:** Enumerate move sequences; repeated states grow exponentially without visited tracking.

## Why it works

Every legal one-turn neighbor is generated, including wraparound. BFS layers count turns, and deadend states are never entered. The first target layer is optimal. S is state count, D deadend count, and constructing each neighbor copies L characters.

## Complexity

O(D L + S L²) expected time, including deadend hashing, for S at most 10000 states and L = 4. Python uses O(S L + D) auxiliary space; its deadend set retains references to input strings. C++ copies deadend strings and uses O(S L + D L) auxiliary space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

The start is unusable when it is a deadend, even if it equals the target. The independent integer-state reference uses bidirectional search. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Use a target-directed heuristic and compare explored state counts.

## Python and C++23 comparison

C++ stores string states in hash sets and a queue and accepts the target by reference. Its modular digit expression adds ten before remainder to avoid a negative C++ remainder on decrementing zero. Both versions preserve deadends and target.

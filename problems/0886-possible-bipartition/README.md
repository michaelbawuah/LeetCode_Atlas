# 886 · Possible Bipartition

[Problem](https://leetcode.com/problems/possible-bipartition/) · Medium

## Idea and approach

Build an undirected dislike graph and assign opposite colors across every edge.

**Baseline:** Enumerate all binary group assignments and check dislikes.

## Why it works

Each chosen starting color determines the required relative colors throughout its component. A same-color edge contradicts the required separation. If no conflict occurs, the two color classes satisfy every dislike, including disconnected components.

## Complexity

O(n + E) time. O(n + E) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

A conflict outside the component of person one still makes the whole partition impossible. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Return both groups or an odd cycle explaining failure.

## Python and C++23 comparison

Both versions build symmetric adjacency lists and color disconnected components. C++ uses signed integer colors ±1 and a queue. Time and auxiliary storage are O(n+E); dislike pairs are not changed.

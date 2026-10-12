# 1319 · Number of Operations to Make Network Connected

[Problem](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) · Medium

## Idea and approach

Check the necessary total cable count, then union existing links and connect the remaining components with spare cables.

**Baseline:** Compute all-pairs connectivity and identify component representatives.

## Why it works

Every connected n-node network needs at least n−1 cables. In a network with C components, a spanning forest uses n−C cables, leaving E−(n−C) movable extras. E≥n−1 makes at least C−1 extras available, exactly enough to join the components.

## Complexity

O((n + E) alpha(n)) amortized time. O(n) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

A large connected component cannot compensate for fewer than n−1 total cables. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** List cable removals and new links realizing the minimum.

## Python and C++23 comparison

C++ checks the total cable count before allocating its parent and size vectors. With union by size and path compression, both versions take O((n+E) α(n)) amortized time and O(n) space; connections remain unchanged.

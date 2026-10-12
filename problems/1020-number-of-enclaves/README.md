# 1020 · Number of Enclaves

[Problem](https://leetcode.com/problems/number-of-enclaves/) · Medium

## Idea and approach

Flood-fill land reachable from any border, then count land outside that visited set.

**Baseline:** Label every land component and sum the sizes of those having no border member.

## Why it works

The traversal finds exactly cells with a land path to the edge. Every unvisited land cell lacks such a path and is an enclave; counting cells rather than components gives the required area total.

## Complexity

O(R C) time. O(R C) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

The answer is the number of trapped land cells, not the number of trapped islands. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Return enclave components and their separate areas.

## Python and C++23 comparison

C++ uses an explicit byte visited matrix and coordinate stack. Both versions keep the grid unchanged, use O(R C) auxiliary space, and count unescaped cells rather than components.

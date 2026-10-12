# 947 · Most Stones Removed with Same Row or Column

[Problem](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) · Medium

## Idea and approach

Union distinct row and column identities for every stone; count the resulting stone-connected components.

**Baseline:** Build the O(N²) graph linking stone pairs that share a row or column.

## Why it works

Rows and columns use separate namespaces. Their union graph connects exactly stones linked through row/column-sharing chains. At least one stone must remain per component. Removing leaves of any component spanning tree removes all others legally, making N minus component count achievable.

## Complexity

O(N alpha(N)) expected amortized time. O(N) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Using the same identity for row 2 and column 2 creates false connections. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Output a legal removal order using a component spanning tree.

## Python and C++23 comparison

C++ encodes row x as 2x and column y as 2y+1, keeping namespaces disjoint within the official nonnegative coordinate bounds. Union by size and path compression give expected amortized O(N α(N)) time and O(N) space. Input coordinates are unchanged.

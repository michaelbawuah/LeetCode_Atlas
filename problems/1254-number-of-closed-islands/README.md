# 1254 · Number of Closed Islands

[Problem](https://leetcode.com/problems/number-of-closed-islands/) · Medium

## Idea and approach

Traverse each zero-valued land component and remember whether any member touches a grid edge.

**Baseline:** Union land cells with an explicit outside vertex and count components separate from it.

## Why it works

Flood-fill identifies one whole connected land component at a time. It is closed exactly when none of its members has an edge location. Each component starts once, so adding only those with no boundary member counts every closed island once.

## Complexity

O(rows * cols) time. O(rows * cols) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Here zero means land and one means water, opposite to several neighboring island problems. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Return each closed island’s area and bounding box.

## Python and C++23 comparison

Both sources mark a zero-valued component visited, explore it iteratively, and retain whether it touches a border. C++ uses an owned seen matrix and traversal stack and leaves the input grid unchanged. O(rows × cols) time and auxiliary storage exclude the runner’s input copy. Marking before pushing prevents repeated discovery, and standard containers release all owned state after each case.

# 310 · Minimum Height Trees

[Problem](https://leetcode.com/problems/minimum-height-trees/) · Medium

## Idea and approach

Repeatedly remove all current tree leaves until only one or two centers remain.

**Baseline:** Measure the rooted height from every vertex in O(n²) time.

## Why it works

Every longest tree path has leaves at both ends. Removing one outer layer shortens all eccentricities of surviving vertices uniformly, so the height-minimizing centers stay unchanged. A tree has one center or two adjacent centers; these are precisely the final vertices.

## Complexity

O(n) time. O(n) auxiliary; O(1) roots output space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

Processing newly formed leaves in the same round can strip past the center; queue rounds must use their original sizes. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Compute the minimum height itself from the number of removed layers.

## Python and C++23 comparison

The C++ queue peels fixed-size rounds just as Python deque does, with O(n) adjacency, degree, and queue storage; a tree yields at most two output roots.

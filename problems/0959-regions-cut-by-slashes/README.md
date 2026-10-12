# 959 · Regions Cut By Slashes

[Problem](https://leetcode.com/problems/regions-cut-by-slashes/) · Medium

## Idea and approach

Split every square into top, right, bottom, and left triangles; union triangles connected without crossing a slash and across neighboring square boundaries.

**Baseline:** Rasterize each cell into a 3×3 wall image and flood-fill all open regions.

## Why it works

A slash separates exactly two pairs of triangles, while a blank connects all four. Boundary unions represent every permitted crossing between squares. DSU components therefore match precisely connected open regions.

## Complexity

O(n^2 alpha(n^2)) amortized time. O(n^2) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

A diagonal wall needs sufficient raster resolution in the reference; corner pixels alone can leak across slashes. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Measure which regions touch the outer grid boundary.

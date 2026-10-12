# 304. Range Sum Query 2D - Immutable

[Problem on LeetCode](https://leetcode.com/problems/range-sum-query-2d-immutable/) · Medium

## Approach, invariant, and complexity

Precompute the sum above and left of every boundary. Four prefix rectangles then describe any queried rectangle by inclusion and exclusion.

A baseline scans every requested rectangle, O(mn) worst-case query time. Each prefix entry stores exactly the rectangle from the origin through its preceding cell: adding the top and left prefixes double-counts their overlap, so subtract it once. Applying the same identity to query boundaries removes the two outside strips and restores their overlap.

Construction takes O(mn) time and space; each sumRegion takes O(1). The extra zero border makes first-row and first-column queries use the same formula. Public query endpoints are inclusive.

Negative entries are valid. Allocate separate prefix rows, avoiding Python list-aliasing. The input matrix is preserved and the data structure is immutable after construction.

Follow-up: support point updates without rebuilding all prefixes. Compare a two-dimensional Fenwick tree with this static representation.

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

## C++23 counterpart

C++ stores int64_t prefix totals so inclusion-exclusion arithmetic is widened before addition and subtraction. Under the problem bounds m,n<=200 and absolute cell value<=10000, a rectangle total is at most 400000000 in magnitude and safely returns int. The matrix is borrowed during construction and never modified; prefixes own their storage.

Time: constructor O(mn); sumRegion O(1). Space: O(mn).

The JSON adapter creates fresh state per case. Named fixtures and 150 deterministic generated inputs compare the two language implementations; existing independent Python oracles supply a separate behavioral reference.

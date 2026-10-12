# 74. Search a 2D Matrix

[Problem on LeetCode](https://leetcode.com/problems/search-a-2d-matrix/) · Medium

## Intuition
The row-order guarantees make the entire matrix sorted when read row by row. A virtual flat index can access that sequence without copying it.

## Approaches
- **Baseline:** inspect all cells: O(mn) time and O(1) extra space.
- **Optimized:** binary search the virtual flattened order, translating each middle index into a row and column.

## Correctness invariant
If the target is present and not yet returned, one matching cell lies inside the half-open virtual interval `[left, end)`. Global row-major order permits discarding the half excluded by each comparison. The middle is translated with `row = index // columns` and `column = index % columns`, so the comparison accesses the corresponding matrix cell exactly.

## Complexity
O(log(mn)) time and O(1) extra space for m rows and n columns. The matrix is not flattened into a new list.

## Edge cases and pitfalls
Handle one row, one column, and one cell with the same index formula. Duplicates within a row are allowed. This algorithm relies on each row's first value exceeding the previous row's last value; independently sorted rows and columns alone are insufficient.

## Follow-up
Search a matrix that only has sorted rows and sorted columns. What ordering argument supports starting from a corner?

## Verification
Named fixtures and an independent generated-input reference accompany this implementation. Official judge results are tracked separately in metadata.

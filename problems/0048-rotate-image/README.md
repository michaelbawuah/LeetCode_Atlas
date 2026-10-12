# 48 · Rotate Image

[Problem](https://leetcode.com/problems/rotate-image/) · Medium · In-place matrix transformation

## Approach

**Baseline:** allocate a second n × n matrix and copy each value to its rotated
coordinate, requiring O(n²) extra space.
**Chosen approach:** transpose across the main diagonal, then reverse every row.
Only entries strictly above the diagonal are swapped during transposition.

## Invariant and correctness

Transposition maps the original coordinate `(row, column)` to `(column, row)`.
Reversing rows maps that coordinate to `(column, n - 1 - row)`, exactly a clockwise
quarter-turn. Each off-diagonal pair is swapped once, while the diagonal remains
correct. Row reversal then completes the mapping for every entry.

## Complexity

O(n²) time and O(1) auxiliary space. The matrix and its existing row lists are
mutated; the method returns `None`. Fixture evaluation reads argument zero after mutation.

## Verification and pitfalls

Tests check the independent coordinate mapping, object identities, and restoration
after four rotations. Cover singleton, negative, repeated, and even/odd dimensions.
Swapping every `(row, column)` pair would transpose twice and cancel the change.
The method assumes a square matrix; a rectangular rotation changes dimensions.

**Follow-up:** how would a four-way cycle rotate one layer without transposing?

# 73 · Set Matrix Zeroes

[Problem](https://leetcode.com/problems/set-matrix-zeroes/) · Medium · In-place markers

## Approach

**Baseline:** collect rows and columns containing original zeroes in sets,
requiring O(m + n) extra storage.
**Chosen approach:** use the first column as row markers and the first row as
column markers. Save two booleans for whether those marker units originally contain zeroes.

## Invariant and correctness

After scanning the interior, a zero marker identifies exactly a row or column
that needs clearing because of an original zero. Clearing the interior consults
those markers without changing them. Finally, the saved booleans clear the first
row and column if originally necessary. Separating detection from clearing stops
newly written zeroes from spreading beyond the original affected units.

## Complexity

O(mn) time and O(1) auxiliary space. The original matrix and row objects are
mutated; the method returns `None`. Metadata selects mutated argument zero for fixtures.

## Verification and pitfalls

The oracle gathers affected coordinates from an untouched copy. Cases cover the
origin, one row/column, no zeroes, and multiple zeroes. The `(0, 0)` cell cannot
encode both first-unit flags by itself. A second application can spread newly
created zeroes further, so idempotence is not a valid general property here.

**Follow-up:** how would marking change if the matrix representation were sparse?

## C++23 counterpart

C++ saves the original first-row and first-column conditions before using those cells as markers. No row or column sets are allocated; the method returns `void`, and the adapter reads the mutated matrix. All entries, including signed integer limits, are only compared with zero or replaced by zero, so no arithmetic overflow occurs. Complexity remains O(mn) time and O(1) auxiliary space.

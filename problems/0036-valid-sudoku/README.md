# 36 · Valid Sudoku

[Problem](https://leetcode.com/problems/valid-sudoku/) · Medium · Hash sets

## Idea

A filled digit must be new to three units: its row, column, and 3 × 3 box.
Dots represent unfilled cells and contribute nothing to those units.

**Baseline:** for each filled cell, search its row, column, and box for another
copy. This repeats comparisons.
**Chosen approach:** maintain nine sets per unit type and scan the board once.
The box index is `(row // 3) * 3 + column // 3`.

## Why it works

Before a cell is visited, each set contains exactly the filled digits already
seen in its unit. A repeated membership proves a rule violation. Otherwise,
inserting the digit maintains that invariant. Any duplicate pair is detected
when its later cell is visited, regardless of which unit contains it.

## Complexity

For the fixed 9 × 9 board, time and auxiliary space are both O(1): at most 81
cells and 27 sets with at most nine digits each. These bounds rely on the fixed
board size rather than describing an arbitrary-size Sudoku solver.

## Tests and pitfalls

Fixtures isolate row, column, and box duplicates, and include a valid completed
grid and one with holes. Properties validate independently collected units and
remove random cells from a valid grid. Repeated digits in unrelated units are allowed.
Validity checks the filled cells; it does not prove that a partial board has a solution.

**Follow-up:** how would candidate sets and backtracking extend this into a solver?

## C++23 counterpart

C++ uses three zero-initialized 9×9 boolean tables instead of hash sets. The contract restricts each cell to a dot or digit 1–9; dots are skipped before indexing the digit table. The adapter converts the one-character JSON strings to the standard `vector<vector<char>>` interface. These fixed tables keep time and auxiliary space O(1), and the board is preserved.

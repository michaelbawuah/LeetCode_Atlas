# 6. Zigzag Conversion

[Problem on LeetCode](https://leetcode.com/problems/zigzag-conversion/) · Medium

## Approach

A full coordinate grid stores unused cells. Retain only actual row characters, moving the active row down and up.

## Invariant and correctness

Each retained row contains exactly the processed characters assigned to that row, in arrival order. Direction reverses only at the two boundaries, following the zigzag path; reading rows produces the required order.

## Complexity

Time: O(n + r). Space: O(n + r).

## Boundaries and pitfalls

Handle one row before changing direction. When rows exceed the string length, reading the rows leaves the string unchanged. r denotes numRows; the guard avoids allocating unnecessary rows.

## Follow-up

Generate the output by periodic index jumps without storing intermediate rows.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

The C++ implementation accumulates row strings with amortized append, reserves the final n-character result, and copies each retained character once into it. n is input length and r is the requested row count; the early guard avoids allocating excess rows.

Time: O(n + r) amortized string appends. Space: O(n + r), including row storage and returned string.

The JSON adapter creates fresh state per case. Named fixtures and 150 deterministic generated inputs compare the two language implementations; existing independent Python oracles supply a separate behavioral reference.

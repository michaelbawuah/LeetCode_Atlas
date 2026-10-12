# 118 · Pascal's Triangle

[Problem](https://leetcode.com/problems/pascals-triangle/) · Easy

## Idea and approaches

Build each triangle row from the two adjacent entries above it. Recomputing each coefficient independently is a baseline; sharing the preceding row directly expresses Pascal recurrence.

## Correctness invariant

The first and last entries of every row are one. Every interior entry is the sum of its two parents. Starting with [1], induction on row number therefore constructs exactly the binomial coefficients of every requested row.

## Complexity

O(r^2) time for r rows. Required output is O(r^2); scalar loop state adds O(1) auxiliary storage. Newly allocated row arrays become part of the output rather than copies of existing rows.

## Verification and pitfalls

Tests use independent binomial coefficients, verify row sums equal powers of two, and ensure rows are distinct list objects. The upper row bound protects integer-range assumptions in C++.

Do not repeat the same mutable row object when constructing several rows. Endpoints must remain one.

**Follow-up:** How could a generator stream rows while retaining only the previous row?

## Python and C++23

C++ allocates output rows directly and reserves the outer vector. All row coefficients fit int for the legal maximum 30 rows. Auxiliary state excludes these required output rows. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.

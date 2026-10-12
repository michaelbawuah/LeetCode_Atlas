# 119 · Pascal's Triangle II

[Problem](https://leetcode.com/problems/pascals-triangle-ii/) · Easy

## Idea and approaches

Generate a single row using the ratio between neighboring binomial coefficients. Building all preceding rows is an O(r^2) baseline; a multiplicative ratio needs only r updates.

## Correctness invariant

The first coefficient is C(r, 0) = 1. If the current coefficient is C(r, j - 1), multiplying by (r - j + 1) and dividing by j yields C(r, j). The division is exact, so induction supplies the entire row without earlier rows.

## Complexity

O(r) time and O(1) auxiliary space excluding O(r) output. Python uses integer multiplication and exact floor division; no floating-point rounding is introduced.

## Verification and pitfalls

The independent oracle repeatedly applies adjacent-addition Pascal expansion. Symmetry and the row sum 2^r are checked. Fixtures include row zero and the maximum legal row index 33.

Multiply before dividing, and use a sufficiently wide intermediate in a fixed-width language even when the final coefficients fit int.

**Follow-up:** How would prime-factor cancellation compute much larger coefficients without intermediate overflow?

## Python and C++23

C++ evaluates coefficient multiplication in long long before exact division and narrows only the final bounded coefficients to int. Row index 33 is included in fixtures; output has O(r) entries. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.

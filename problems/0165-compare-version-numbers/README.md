# 165. Compare Version Numbers

[Problem on LeetCode](https://leetcode.com/problems/compare-version-numbers/) · Medium

## Approach

Comparing version strings lexically gives the wrong numeric order. Parse revisions, compare corresponding integers, and substitute zeros for absent revisions.

## Invariant and correctness

All earlier revision pairs are equal before the current comparison. The first unequal numeric pair determines version order, while no difference after zero-padding proves equality.

## Complexity

Time: O(n + m). Space: O(n + m).

## Boundaries and pitfalls

Leading zeros have no numeric significance. Valid revisions fit signed 32-bit integers; n and m are total input lengths, including parsing and split copies.

## Follow-up

Compare revisions without integer conversion when their digit lengths are unbounded.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

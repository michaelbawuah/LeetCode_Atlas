# 78 · Subsets

[Problem](https://leetcode.com/problems/subsets/) · Medium

## Idea

Begin with the empty subset. For each new value, keep every existing subset and add one copy containing the new value. Each step doubles the answer collection.

**Baseline:** enumerate all bitmasks and reconstruct each selected subset. The chosen iterative expansion expresses the same include-or-exclude decisions directly with list copies.

## Why it works

After processing i values, answers contain every subset of those values exactly once. For the next value, subsets partition into those excluding it, already present, and those including it, formed by appending it to each old subset. The classes are disjoint, and distinct input values prevent duplicate subsets.

## Complexity

O(n 2^n) time and O(n 2^n) total storage, including the required output. Building additions uses a temporary list whose subsets become output entries. The input is preserved.

## Counterexample and checks

Appending to old subset objects would alter previously emitted answers and break the partition invariant. Each addition creates a new list. The independent oracle enumerates combinations separately for every subset size and verifies the 2^n count. The empty subset belongs to every result, even though LeetCode's input itself has at least one value.

**Follow-up:** return only subsets of exactly size k, and prune choices that cannot reach k.

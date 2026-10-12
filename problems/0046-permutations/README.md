# 46 · Permutations

[Problem](https://leetcode.com/problems/permutations/) · Medium

## Idea

Fix one position at a time by swapping each remaining value into it. Undo every swap after exploring its branch, so sibling branches begin from the same state.

**Baseline:** enumerate all n^n length-n index sequences and filter those with no repeated index. Backtracking produces only prefixes with distinct selected values.

## Why it works

At depth i, the first i positions are fixed and the suffix contains exactly the remaining values. Each possible suffix value is placed at position i once. Induction on the suffix length shows every full ordering is generated once. The contract requires distinct input values, so different choices cannot yield the same permutation.

## Complexity

There are n! results, each copied in O(n) time: O(n n!) total time and output storage. A private input copy and recursion stack require O(n) auxiliary space. Input is not modified.

## Counterexample and checks

Storing the same mutable list repeatedly makes all results reflect later swaps. Copy each completed ordering, and undo swaps when returning. Tests compare against an independent exhaustive iterator and check the factorial result count. Outer answer order is arbitrary; order within each permutation is essential.

**Follow-up:** how should branches be deduplicated when input values can repeat?

## Python and C++23 comparison

Both versions swap values in a private copy and undo each swap after returning from a branch. C++ appends a new copied vector for every complete permutation, while Python appends a new copied list. Time is O(n n!), auxiliary copy and recursion storage O(n), and result storage O(n n!). The caller's input order is preserved.

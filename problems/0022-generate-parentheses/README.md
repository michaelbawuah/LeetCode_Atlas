# 22 · Generate Parentheses

[Problem](https://leetcode.com/problems/generate-parentheses/) · Medium

## Idea

Build only prefixes that can still become a balanced string. Add an opening parenthesis while fewer than n have been used; add a closing one only when it has an unmatched opening partner.

**Baseline:** enumerate all 2^(2n) parenthesis strings and validate them. Backtracking prunes invalid prefixes immediately.

## Why it works

Every constructed prefix satisfies 0 ≤ closed ≤ opened ≤ n, so its balance never becomes negative. Reaching closed = n also forces opened = n, producing a balanced string of exactly n pairs. Every valid string obeys these prefix inequalities, so none of its choices are pruned. Each character sequence follows one unique branch.

## Complexity

There are C_n valid results, the nth Catalan number. Runtime and output storage are O(n C_n); each result has 2n characters. The mutable path and recursion stack take O(n) auxiliary space.

## Counterexample and checks

Equal opening and closing counts alone do not imply validity: `)(` has matching counts but a negative first prefix. The independent oracle enumerates all binary strings at small n, checks every prefix, and compares complete result sets. A separate n = 8 check validates the Catalan count and uniqueness.

**Follow-up:** support several bracket types and explain how nesting changes the state.

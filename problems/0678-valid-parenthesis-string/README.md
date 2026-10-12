# 678 · Valid Parenthesis String

[Problem](https://leetcode.com/problems/valid-parenthesis-string/) · Medium

## Idea

Instead of choosing a meaning for each wildcard, track the smallest and largest feasible unmatched-opening counts. The feasible balances form an interval.

**Baseline:** enumerate each wildcard as empty, opening, or closing, requiring up to 3^w expansions. Two interval endpoints summarize those possibilities.

## Why it works

An opening shifts every balance upward; a closing shifts every balance downward and invalidates negative outcomes. A wildcard unions the three neighboring shifts, preserving an interval after clipping below zero. A negative maximum means no interpretation survives that prefix. At the end, zero is feasible exactly when the clipped minimum is zero.

## Complexity

O(n) time and O(1) auxiliary space, with boolean output and unchanged input.

## Counterexample and checks

A wildcard before a later opening cannot retroactively close it: `*(` is invalid despite enough apparent wildcard capacity. The oracle independently enumerates wildcard replacements and verifies every prefix balance.

**Follow-up:** return one valid wildcard assignment in addition to the boolean answer.

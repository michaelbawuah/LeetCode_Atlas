# 2115 · Find All Possible Recipes from Given Supplies

[Problem](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/) · Medium

## Idea and approach

Index recipes waiting on each ingredient and release a recipe when all required ingredients have become available.

**Baseline:** Repeatedly scan every recipe until no new recipe can be made.

## Why it works

The queue contains newly available supplies or completed recipes. Each occurrence in a dependency list decrements one unmet requirement exactly once. A recipe reaches zero only after every ingredient is available; enqueuing it allows its downstream dependents to progress. Unresolvable cycles remain unmet. I counts ingredient occurrences; S supplies and R recipes.

## Complexity

O(I + S + R) expected time. O(I + S + R) auxiliary; O(R) output space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

A recipe appearing as an ingredient does not make it available before its own requirements finish. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Return a dependency explanation for every recipe that remains unavailable.

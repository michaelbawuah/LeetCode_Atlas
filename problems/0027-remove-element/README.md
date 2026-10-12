# 27 · Remove Element

[Problem](https://leetcode.com/problems/remove-element/) · Easy

## Idea and approaches

Write every non-target value into the next retained slot. A baseline filters into a new list in O(n) extra space; this compaction uses the original list.

## Correctness invariant

The written prefix contains exactly the non-target values from the processed input prefix. The write index never exceeds the read index, so overwriting cannot affect a future unread value. At completion its length is the number of retained elements.

## Complexity

O(n) time and O(1) auxiliary space. The method returns k and mutates the first k slots; ordering is unrestricted by the problem, although this implementation preserves it.

## Verification and pitfalls

Generated tests check the actual returned k and mutated prefix against filtering, preserving multiplicities and allowing any valid prefix order. Empty input, all removed, and no removed elements are named cases.

Do not remove list items while scanning, which shifts indices and can make the process quadratic. The tail after k is irrelevant.

**Follow-up:** How does swapping unwanted values with the last active slot trade stable order for fewer writes?

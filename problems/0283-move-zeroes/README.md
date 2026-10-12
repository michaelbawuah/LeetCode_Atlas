# 283 · Move Zeroes

[Problem](https://leetcode.com/problems/move-zeroes/) · Easy · In-place compaction

## Idea

Keep a write pointer for the next nonzero position. Read values in order, write
each nonzero into that prefix, then fill the remaining positions with zeroes.

**Baseline:** build a new list of nonzero values followed by zeroes, requiring
O(n) extra space.
**Chosen approach:** compact into the original list using two indices and a final
zero-fill pass. The method returns `None`, as required for in-place mutation.

## Why it works

Before each read step, the prefix before `write` contains exactly the nonzero
values encountered so far, in their original order. Also `write <= read`, so
writing cannot overwrite an unread future value. Appending each encountered
nonzero preserves this invariant. After scanning, the remaining positions are
precisely the number of zeroes originally present; filling them completes the result.

## Complexity

O(n) time and O(1) auxiliary space. The list length and identity are preserved.

## Tests and pitfalls

Fixtures cover all-zero, no-zero, signed, boundary-integer, and interleaved arrays.
Properties compare against stable filtering, check a `None` return, and check
idempotence. Metadata declares `result_from_arg: 0` so fixture evaluation compares
the mutated array. Assigning `nums` to a new list would not update the caller's list.

**Follow-up:** how can swapping reduce writes when zeroes are rare?

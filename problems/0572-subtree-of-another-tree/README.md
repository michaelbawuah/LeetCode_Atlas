# 572 · Subtree of Another Tree

[LeetCode problem](https://leetcode.com/problems/subtree-of-another-tree/)

## Intuition
A candidate root must start a complete structural match, including absent children; matching a few values does not suffice.

## Baseline and approach
Check the smaller tree against each root position in the larger tree. Both the candidate scan and exact comparison use explicit stacks. Value matching skips unnecessary comparisons, although repeated values can still force the worst case. Both supplied roots are nonempty under this problem's constraints.

## Why it works
The scan reaches every possible subtree root. The comparison accepts only when all corresponding values and child positions agree. Therefore an acceptance exhibits the required subtree, and exhausting all candidates proves none exists.

## Complexity
For n main-tree nodes, m smaller-tree nodes, and heights h and hs: **O(n × m) worst-case time, O(h+hs) auxiliary space**. Candidate comparisons occur one at a time. A successful comparison visits m matching nodes; a failed one stops at a mismatch.

## Pitfalls
A candidate with extra descendants is not equal to the smaller tree. Repeated root values require continuing after an unsuccessful candidate. Do not use a serialization that omits null positions.

## Follow-up
Serialize values with explicit null tokens, then use a linear-time sequence matcher to obtain O(n+m) time.

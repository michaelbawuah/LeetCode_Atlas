# 38. Count and Say

[Problem on LeetCode](https://leetcode.com/problems/count-and-say/) · Medium

## Approach

Repeated single-character string concatenation can copy growing outputs quadratically. Gather one count/symbol pair per run and join once.

## Invariant and correctness

The completed pieces describe exactly the processed runs, and start is the first undescribed character. Extending end through equal characters identifies the next maximal run, preserving the invariant.

## Complexity

Time: O(S), S is total length of generated terms. Space: O(L), L is maximum generated term length.

## Boundaries and pitfalls

A term describes contiguous runs, not total character frequencies. Account for output growth rather than treating n iterations as constant-cost.

## Follow-up

Return the run-length pairs before converting them to the next string.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

# 583 · Delete Operation for Two Strings

[LeetCode problem](https://leetcode.com/problems/delete-operation-for-two-strings/)

## Intuition
The characters retained in both strings must form a common subsequence.

## Baseline and approach
Enumerating retained index subsets is exponential. A rolling LCS table finds the maximum number of characters that can stay.

## Why it works
Any valid deletion outcome is a common subsequence, so it cannot retain more than the LCS. Conversely retaining an LCS deletes exactly m+n−2L characters, producing identical strings. Minimizing deletions is therefore equivalent to maximizing L.

## Complexity
Python: **O(m n) time; O(min(m, n)) auxiliary space**. m and n are string lengths. O(mn) time and O(min(m,n)) storage include rolling states. Python swaps references; C++ selects const references to avoid input-string copies.

## Pitfalls
Only deletions are allowed; replacement is not one operation in this problem. Repeated letters count by position and must preserve order.

## Follow-up
How would per-character deletion costs change the retained-subsequence objective?

## C++23 counterpart
**O(m n) time; O(min(m, n)) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

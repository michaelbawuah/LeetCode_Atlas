# 712 · Minimum ASCII Delete Sum for Two Strings

[LeetCode problem](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)

## Intuition
Keeping matching characters costs nothing; deleting either newest character pays its ASCII value.

## Baseline and approach
Enumerating common retained subsequences is exponential. Weighted prefix DP chooses the cheapest final deletion while retaining matching endpoints.

## Why it works
Each prefix-pair optimum either matches equal newest characters using the diagonal state or deletes one endpoint using an adjacent state plus its value. These choices cover all possible final actions. Boundary sums delete every character of the unmatched prefix.

## Complexity
Python: **O(m n) time; O(min(m, n)) auxiliary space**. m and n are lengths. Both versions use O(mn) time and O(min(m,n)) row storage without copying input strings. C++ converts ASCII characters through unsigned char; official lowercase lengths bound the total cost by 244,000.

## Pitfalls
Character values are weights, so maximizing common-subsequence length alone is insufficient. Matching order still matters. Preserve old and current rows correctly.

## Follow-up
How would the algorithm adapt to arbitrary nonnegative character weights?

## C++23 counterpart
**O(m n) time; O(min(m, n)) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

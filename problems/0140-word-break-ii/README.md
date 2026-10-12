# 140 · Word Break II

[LeetCode problem](https://leetcode.com/problems/word-break-ii/)

## Intuition
First identify suffixes that can finish a sentence. Then enumerate only word choices whose remaining suffix is feasible.

## Baseline and approach
Trying all partition masks and checking their words is the baseline. A suffix DP prunes dead branches before a backtracking traversal builds complete sentences.

## Why it works
The suffix table is computed from right to left: a suffix is feasible exactly when it begins with a dictionary word followed by a feasible suffix. During enumeration, path contains a valid segmentation of the consumed prefix. Every chosen next word passes the suffix test, and every legal complete segmentation follows one enumerated cut sequence. Distinct cut sequences produce distinct sentences.

## Complexity
With n input characters, maximum word length L, dictionary size W, total dictionary characters T, and K sentences, a conservative bound is **O(T+nL²+L²2^n+Kn) expected time**. Slice copying/hashing is included. **O(W+n+L) auxiliary space** covers the set, suffix table, recursion, and current path; output uses **O(Kn)** space. Exponential work is unavoidable when the output itself is large.

## Pitfalls
Sentence order is unrestricted, but word order inside a sentence is essential. Word reuse is allowed. An impossible suffix should stop exploration; merely caching prefixes cannot remove exponential output size.

## Follow-up
How would you enumerate sentences lazily when materializing every answer is too expensive?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.

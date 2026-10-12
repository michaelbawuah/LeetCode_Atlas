# 10. Regular Expression Matching

[Problem on LeetCode](https://leetcode.com/problems/regular-expression-matching/) · Hard

## Approach, invariant, and complexity

Track whether each string prefix fully matches each pattern prefix. A star either skips its preceding atom or consumes one matching character while retaining the same pattern prefix.

A baseline backtracking matcher may explore exponentially many alternatives. Dynamic programming merges equivalent prefix states. For a non-star atom, matching consumes one character and one pattern atom. For a star, the two transitions enumerate exactly zero repetitions or at least one repetition. Initialization accounts for star groups that match an empty prefix.

For string length m and pattern length p, time is O(mp) and auxiliary space O(p), retaining only the previous row and the current row. Pattern validity guarantees each star has a preceding atom.

This is full-string matching, not substring search. Dot matches one character; star repeats its previous atom, rather than standing for an arbitrary wildcard by itself.

Follow-up: add a plus quantifier requiring one or more repetitions. Which transition loses its zero-repetition branch?

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

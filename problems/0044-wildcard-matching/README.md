# 44 · Wildcard Matching

[LeetCode problem](https://leetcode.com/problems/wildcard-matching/)

## Intuition
A wildcard star can match no character or extend its match by one character.

## Baseline and approach
Backtracking over every star length is exponential. Prefix DP uses a previous row for the text prefix and a current row for the next character.

## Why it works
A star cell is reachable from the current row’s left cell by matching nothing, or from the previous row’s same column by consuming the new character. A literal or question mark instead requires the diagonal prefix to match. These alternatives cover every possible last action, including a pattern made only of stars on empty text.

## Complexity
Python: **O(m n + m + n + 1) time; O(n + 1) auxiliary space**. m and n are text and pattern lengths. O(n) pattern states are retained; patterns cannot be swapped with text to shorten the row. Boundary initialization accounts for empty inputs.

## Pitfalls
This star matches any sequence, unlike a regular-expression star that repeats its preceding token. Match the whole text and pattern. Empty strings and consecutive stars are valid.

## Follow-up
What invariant makes a greedy algorithm with one remembered star position correct?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

## C++23 counterpart

For text length m and pattern length n, two packed Boolean rows retain O(n + 1) states. By-value string copies occupy O(m + n) bytes and are included in the C++ space bound. Empty text/pattern and repeated stars remain valid. This star consumes arbitrary text rather than repeating a preceding regular-expression atom.

C++: **O(m n + m + n + 1) time; O(m + n + 1) including string copies; O(n + 1) DP states space**. Named fixtures and 150 reproducible generated inputs compare this implementation with the Python track.

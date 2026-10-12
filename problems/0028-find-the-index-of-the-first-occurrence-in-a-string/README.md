# 28. Find the Index of the First Occurrence in a String

[Problem on LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) · Easy

## Approach

Trying every start can cost O(nm). KMP records the longest proper prefix that is also a suffix at each pattern position, then reuses it after mismatches.

## Invariant and correctness

matched is the longest pattern prefix matching a suffix of the consumed text. A mismatch follows failure links to shorter feasible suffixes; a matching character extends the surviving prefix. The first full prefix reached ends the earliest occurrence.

## Complexity

Time: O(n + m). Space: O(m).

## Boundaries and pitfalls

Build failure values from previous values, not from text matches. n and m are text/pattern lengths. Named and generated inputs use nonempty lowercase strings.

## Follow-up

Find all matches, including overlapping occurrences, by following the failure link after recording each full match.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

Both versions preserve input unless the problem specifies mutation. C++ string arguments use const references; adapter-decoded inputs are separately owned and excluded from solution auxiliary space.

Time: O(n + m). Space: O(m).

# 981. Time Based Key-Value Store

[Problem on LeetCode](https://leetcode.com/problems/time-based-key-value-store/) · Medium

## Approach, invariant, and complexity

Each key owns a timestamp-ordered history. Strictly increasing set timestamps permit appending; an upper-bound search finds the last timestamp no later than a query.

A baseline scans the entire key history, O(h) per query. Binary search takes O(log h), while appending takes O(1) amortized expected time. Stored space is O(S) for S set records, including their key/value data in the bounded-string model. A query boundary divides history into eligible and future records; the last eligible record is exactly the required value.

An unknown key or a query before its first timestamp returns the empty string. A query equal to a set timestamp includes that record. The ordering guarantee is essential to the append-only representation.

Follow-up: accept out-of-order writes. Compare sorted insertion with a balanced search tree.

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp)

The C++ implementation uses timestamp vectors and upper_bound. Returned strings are copied; key/value hashing and copying add their string-length costs.

Time: set O(|key| + |value|) amortized expected; get O(|key| + log h + |answer|) expected. Space: O(S). The local adapter constructs a fresh object for each fixture and owns any converted inputs.

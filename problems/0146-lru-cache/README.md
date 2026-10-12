# 146. LRU Cache

[Problem on LeetCode](https://leetcode.com/problems/lru-cache/) · Medium

## Approach, invariant, and complexity

Maintain a mapping in least-to-most-recent order. A successful read and every write move their key to the recent end; overflow evicts the other end.

A baseline list of keys requires O(capacity) work to locate and move a key. OrderedDict combines hash lookup with linked ordering: O(1) expected work per operation and O(capacity) stored space. Its order exactly matches the relative order of successful accesses, so the first entry is precisely the key that must be evicted.

Missing reads do not alter recency. Updating an existing key must count as access without consuming an extra capacity slot. Capacity is positive under the contract.

Follow-up: add time-based expiry while preserving the recency policy. Which index would locate expired entries efficiently?

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp)

The C++ implementation uses a list with hash-indexed iterators. List splicing preserves iterator validity; stored entries are owned by standard containers.

Time: O(1) expected get/put. Space: O(capacity). The local adapter constructs a fresh object for each fixture and owns any converted inputs.

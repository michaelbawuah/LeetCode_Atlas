# 1146. Snapshot Array

[Problem on LeetCode](https://leetcode.com/problems/snapshot-array/) · Medium

## Approach, invariant, and complexity

Record only changes at each index. A snapshot consumes an ID instead of copying the entire array; binary search retrieves the last change at or before an older ID.

A baseline copies length values on every snap, O(length) time and space per snapshot. Each index history here has increasing snapshot IDs, with at most one record for the current unsnapped ID. Overwriting that record coalesces repeated writes. The latest record whose ID does not exceed a query is exactly the value visible at that snapshot.

Construction takes O(length) time. set and snap take O(1) amortized time; get takes O(log h) for h records at that index. Stored space is O(length + U) for retained change records U. snap itself does not duplicate histories.

Initialize every index to zero. Unsnapshotted writes must not change old snapshots. get only receives an already returned snapshot ID.

Follow-up: branch a new writable array from an older snapshot. Which persistent data structure supports sharing unchanged parts?

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

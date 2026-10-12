# 763 · Partition Labels

[Problem](https://leetcode.com/problems/partition-labels/) · Medium

## Idea

A partition containing a character must extend through that character's last occurrence. Keep extending the current end until every encountered character finishes within it, then cut immediately.

**Baseline:** enumerate every possible cut mask and reject cuts splitting a character's occurrences. Last-occurrence boundaries avoid that exponential search.

## Why it works

The current end is a lower bound forced by characters already in the partition. Each newly scanned character may extend that bound. When the scan reaches it, no character in the partition occurs later, so a cut is legal. Cutting at this earliest legal point preserves all future legal cuts and maximizes the total partition count.

## Complexity

O(n) expected time with dictionary operations. O(σ) auxiliary last-occurrence storage and O(p) output for p partitions; the lowercase-English contract bounds σ by 26. The string is unchanged.

## Counterexample and checks

Cutting at a character's first repeated appearance fails when another copy appears farther right. Generated tests enumerate all cut masks and choose a valid partitioning with the largest part count. The output lengths remain ordered because they describe contiguous pieces of the original string.

**Follow-up:** emit the partition substrings and account for their copied character storage.

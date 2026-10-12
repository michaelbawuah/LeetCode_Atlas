# 846 · Hand of Straights

[Problem](https://leetcode.com/problems/hand-of-straights/) · Medium

## Idea

The smallest remaining card must begin a consecutive group because no smaller remaining value can precede it. Start as many groups there as its frequency requires and subtract that multiplicity from every needed consecutive value.

**Baseline:** enumerate partitions of card indices into candidate groups. Sorted frequency consumption makes the smallest-card requirement explicit.

## Why it works

If the smallest remaining value appears g times, every copy needs a group beginning there. Each next value through start+groupSize−1 must therefore have at least g copies. Failure proves no partition exists; subtracting g constructs those groups and leaves the same problem on the remaining multiset. Repeating this invariant uses every card exactly once.

## Complexity

For N cards and u distinct values, O(N + u log u) expected time and O(u) auxiliary space. Successful counter visits each consume at least one card, so their total is O(N); a failing group scans at most N entries after divisibility is checked. The sorted keys and counter use O(u) storage. The hand list is unchanged.

## Counterexample and checks

Divisibility alone does not establish valid groups: `[1, 1, 2, 3]` cannot form two consecutive pairs. The independent oracle tries index-based group partitions, accounting for duplicates individually, instead of making the greedy smallest-value choice.

**Follow-up:** allow groups of several permitted lengths and identify why the same greedy proof no longer follows.

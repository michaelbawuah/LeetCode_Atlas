# 649. Dota2 Senate

[Problem on LeetCode](https://leetcode.com/problems/dota2-senate/) · Medium

## Approach

Simulating each round with marked senators scans inactive entries. Separate queues store only surviving next-turn positions.

## Invariant and correctness

The smaller next-turn index acts first and bans the earliest opponent, preventing the nearest possible opposing action. The survivor moves to the next round by adding n. Banning a later opponent cannot prevent an earlier hostile action, so the earliest ban is safe. Every iteration removes one opponent permanently.

## Complexity

Time: O(n). Space: O(n).

## Boundaries and pitfalls

Queues must retain round order, not just party counts. At most n-1 bans occur, giving linear total work.

## Follow-up

Return the elimination order as well as the winning party.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

# 55 · Jump Game

[Problem](https://leetcode.com/problems/jump-game/) · Medium

## Idea

Track the farthest reachable position while scanning left to right. An index beyond that position is an uncrossable gap; otherwise its jump length can extend the frontier.

**Baseline:** explicitly mark every destination reachable from every earlier position, requiring O(n²) time. A single frontier summarizes those reachable positions.

## Why it works

Reachability from a processed index includes every intermediate landing index up to its maximum jump. Thus all reachable positions discovered so far form a prefix ending at furthest. If the next index lies outside that prefix, no earlier jump reaches it or any later index. If the frontier reaches the last index, a route exists.

## Complexity

O(n) time and O(1) auxiliary space, with boolean output. The input is unchanged.

## Counterexample and checks

A zero does not automatically block progress: `[2, 0, 0]` can jump over it. The independent oracle builds an explicit reachable-position table for small generated arrays.

**Follow-up:** count distinct routes when landing exactly on the last index is required.

## Python and C++23 comparison

Both versions compress reachable positions into a farthest prefix endpoint and return as soon as the last index is covered. C++ represents positions with `size_t`; the contract's nonnegative jump lengths permit conversion before adding a jump. Time is O(n), auxiliary space O(1), and the input is unchanged.

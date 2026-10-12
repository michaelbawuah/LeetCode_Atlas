# 45 · Jump Game II

[Problem](https://leetcode.com/problems/jump-game-ii/) · Medium

## Idea

Every index reachable in a fixed number of jumps forms a prefix. Scan the current frontier and collect the farthest next frontier; crossing a frontier boundary consumes one jump.

**Baseline:** BFS the explicit index graph, potentially examining O(n²) edges. The greedy version compresses each BFS layer into one end index.

## Why it works

Before a boundary is crossed, furthest is the largest endpoint reachable by jumping from any scanned index in the current layer. Once every index through layer_end has been scanned, no path with the current jump count can extend farther. Advancing to furthest therefore creates exactly the next shortest-distance layer. The contract guarantees the last index is reachable.

## Complexity

O(n) time, O(1) auxiliary state, and scalar output. The array is not modified.

## Counterexample and checks

Always jumping to the farthest immediate landing index can lose a better next jump. For `[2, 3, 1, 1, 4]`, landing at index 1 beats landing at index 2. Generated tests compare with explicit BFS and retain only reachable inputs required by the contract.

**Follow-up:** return the sequence of landing indices, not only the minimum count.

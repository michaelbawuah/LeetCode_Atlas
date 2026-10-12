# 994 · Rotting Oranges

[Problem](https://leetcode.com/problems/rotting-oranges/) · Medium

## Idea

All initially rotten oranges spread at the same time. Treat them as simultaneous BFS sources. Each queue layer represents one minute, and a fresh counter detects unfinished work.

**Baseline:** rescan the entire grid for every minute, applying each minute's changes simultaneously. BFS visits each relevant cell once instead.

## Why it works

Before a layer begins, its queue entries are exactly oranges rotten at the previous distance frontier. Their fresh neighbors rot one minute later. Marking them when enqueued prevents double counting. BFS therefore assigns the earliest possible arrival time from any source. Fresh oranges left after the queue empties have no path to a source.

## Complexity

For rows × cols cells, O(rows × cols) time and O(rows × cols) worst-case queue space. The solution changes reachable fresh cells from 1 to 2; the local fixture adapter copies inputs.

## Counterexample and checks

On `[2, 1, 1]`, updating a scan in place can incorrectly infect both fresh cells in one minute. The reference oracle collects each minute's updates before applying them. Cases also cover simultaneous sources, barriers, and grids with no fresh oranges.

**Follow-up:** what changes if crossing different cells takes different amounts of time?

## Python and C++23 comparison

Both versions perform multi-source BFS in fixed-size queue layers, so newly rotten oranges spread in the next minute. Python uses a deque; C++ uses a queue of coordinate pairs. Each fresh cell is marked rotten when enqueued, giving O(rows × cols) time and O(rows × cols) worst-case queue space, with scalar output. Both modify the supplied grid's reachable fresh cells from 1 to 2; local adapters copy the grid before calling either solution.

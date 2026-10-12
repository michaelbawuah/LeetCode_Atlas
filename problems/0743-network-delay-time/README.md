# 743 · Network Delay Time

[Problem](https://leetcode.com/problems/network-delay-time/) · Medium

## Idea

The answer is the largest shortest-path arrival time from the source. Dijkstra's algorithm explores the smallest tentative arrival next because edge delays are nonnegative.

**Baseline:** compute every source-destination distance with Floyd–Warshall in O(V³) time. One-source heap traversal avoids unnecessary source rows.

## Why it works

When the smallest current tentative distance is popped, any alternative path to that vertex must pass through an unprocessed vertex whose tentative distance is no smaller. Nonnegative edges cannot improve that arrival. Relaxing outgoing edges therefore preserves correct shortest distances. Stale heap entries are skipped. The maximum finalized distance is the time all vertices have received the signal; an infinite distance means that goal is impossible.

## Complexity

O((V + E) log(V + 1)) time for the simple directed graph and O(V + E) auxiliary space for adjacency lists, distances, and lazy heap entries. Output is one integer. Times are read without mutation.

## Counterexample and checks

A direct edge of weight 10 can lose to two edges of weight 1; unweighted BFS would be wrong. Zero-weight edges are allowed. Independent generated tests compare against Floyd–Warshall, and named cases exercise stale entries and unreachable vertices.

**Follow-up:** explain what breaks with negative weights and select a suitable replacement algorithm.

## Python and C++23 comparison

Both sources use lazy Dijkstra heaps. C++ uses a min-priority queue of `(time, node)` pairs and reads its adjacency vectors without changing `times`. Under the nonnegative, bounded edge-delay contract, finite shortest-path costs and their relaxations fit `int`. Python uses an infinite float sentinel and integer finite distances; C++ uses `INT_MAX` only for unreachable nodes. Each skips stale entries. Time is O((V+E) log(V+1)), auxiliary storage O(V+E), and output scalar.

# 787 · Cheapest Flights Within K Stops

[Problem](https://leetcode.com/problems/cheapest-flights-within-k-stops/) · Medium

## Idea

At most k stops means at most k+1 flight edges. Keep a minimum-cost table for each allowed edge count, reading the previous table while writing a fresh next table.

**Baseline:** enumerate every bounded walk, with exponential branching. Layered Bellman–Ford shares costs for walks ending at the same city.

## Why it works

After layer t, costs[v] is the minimum cost of reaching v with at most t edges. A valid walk with t+1 edges either already fits layer t or ends with one flight whose prefix fits layer t. Copying the old table preserves the first case and relaxing from old costs covers the second. Reading only the old table prevents one layer from consuming multiple new flights.

## Complexity

O((k+1)(V+E)) time, including O(V) table copies each round, and O(V) auxiliary space for two layers. Output is scalar and the flights are unchanged.

## Counterexample and checks

In-place relaxation can cascade along several input-ordered edges during one round and silently exceed the stop limit. The named four-city chain exposes this bug. Generated tests enumerate all walks capped at k+1 edges, including cycles, independently of the dynamic program.

**Follow-up:** reconstruct a cheapest valid route without losing its edge-count state.

# 332 · Reconstruct Itinerary

[Problem](https://leetcode.com/problems/reconstruct-itinerary/) · Hard

## Idea and approach

Use iterative Hierholzer traversal with each departure heap ordered lexicographically, recording vertices only after their outgoing tickets are exhausted.

**Baseline:** Enumerate ticket-index permutations, filter valid trails, and choose the smallest route.

## Why it works

Every ticket is removed once. Postorder joins completed dead-end trails into the full Euler route. Choosing smallest departures orders available cycle insertions lexicographically, while reverse postorder postpones a departure that would end the itinerary too early. The contract guarantees a trail starting at JFK using every ticket.

## Complexity

O(E log(E + 1)) time. O(E) auxiliary and output space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

A locally smallest destination can lead to an early dead end; returning the forward greedy walk fails the KUL/NRT case. Ticket multiplicities are preserved. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Verify Euler-trail existence before reconstruction when the input contract no longer guarantees it.

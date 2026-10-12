# 2039 · The Time When the Network Becomes Idle

[Problem](https://leetcode.com/problems/the-time-when-the-network-becomes-idle/) · Medium

## Idea and approach

Compute each shortest server distance by BFS, then locate the final resend strictly before its first reply.

**Baseline:** Compute all-pairs distances and explicitly enumerate every sent request until the first response.

## Why it works

A request from distance d receives its reply after 2d units. Resends occur at multiples of patience strictly below 2d, making the last send floor((2d−1)/patience)·patience. Its reply is that send plus 2d; the network is idle one unit after the latest reply across all nodes.

## Complexity

O(V + E) time. O(V + E) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

A response arriving exactly at a resend boundary prevents that resend, which is why the formula uses round-trip minus one. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Support different outbound and inbound transmission latencies.

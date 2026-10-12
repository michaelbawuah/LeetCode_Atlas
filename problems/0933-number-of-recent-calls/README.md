# 933. Number of Recent Calls

[Problem on LeetCode](https://leetcode.com/problems/number-of-recent-calls/) · Easy

## Approach

Scanning the entire timestamp history is O(n) per ping. Increasing timestamps let a deque permanently discard expired calls from its front.

## Invariant and correctness

After cleanup the deque contains exactly recorded timestamps in the inclusive interval [t-3000,t]. Earlier removed times can never become eligible again because t strictly increases.

## Complexity

Time: ping O(1) amortized; O(w) worst case. Space: O(w), retained window calls.

## Boundaries and pitfalls

Keep calls exactly 3000 units old. w is the maximum number of calls retained in an active window over the sequence; each timestamp enters and leaves once.

## Follow-up

Accept out-of-order timestamps using an ordered data structure.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

The C++ design uses standard-container ownership and a fresh local object per fixture. Constructor output is null; these public operations return their integer or Boolean results. Amortized bounds account for container growth/removal; no object persists between fixtures.

Time: ping O(1) amortized; O(w) worst case. Space: O(w), retained window calls.

# 841 · Keys and Rooms

[Problem](https://leetcode.com/problems/keys-and-rooms/) · Medium

## Idea and approach

Traverse directed key edges from room zero, adding each newly unlocked room once.

**Baseline:** Compute every room-to-room reachability relation instead of only the required start.

## Why it works

The visited set contains exactly rooms whose key chain starts at zero. Every newly visited room supplies all its outgoing keys, so traversal closure discovers every visitable room and no inaccessible room.

## Complexity

O(V + E) time. O(V) space. These bounds describe the submitted implementation, excluding fixture-adapter allocations. Inputs are not modified.

## Counterexample and checks

A key inside an inaccessible room cannot help unlock that room or another missing component. Named fixtures cover different structural boundaries. An independent bounded reference accompanies deterministic generated inputs in `test_properties.py`; `parity.py` supplies varied inputs for the shared language checks.

**Follow-up:** Return the shortest sequence of rooms needed to obtain a chosen key.

## Python and C++23 comparison

C++ uses a byte visited vector rather than a Python hash set, with O(V) working space. Both stack traversals mark before insertion, inspect every reachable key once, and leave room lists unchanged.

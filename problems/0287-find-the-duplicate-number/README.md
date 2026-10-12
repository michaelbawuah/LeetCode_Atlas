# 287 · Find the Duplicate Number

[Problem](https://leetcode.com/problems/find-the-duplicate-number/) · Medium

## Idea and approaches

View each array index as a node whose successor is nums[index]. A counting map is an O(n)-space baseline; Floyd cycle detection finds the repeated value without editing input.

## Correctness invariant

The value range 1 through n supplies valid successor indices while the n + 1 positions force a repeated destination. Starting from index zero enters a cycle; its entry is the value with two incoming paths and hence the unique duplicated value. A one-step/two-step meeting locates the cycle, and advancing one pointer from the initial successor with one from the meeting point locates its entry.

## Complexity

O(n) time and O(1) auxiliary space. Both implementations preserve all input entries and keep only scalar indices.

## Verification and pitfalls

Properties use an independent occurrence counter and verify preservation. They vary duplicate multiplicity, including one repeated value appearing many times while other values are absent.

The contract allows the duplicate more than twice. Sorting or sign marking would violate the no-input-modification requirement.

**Follow-up:** How does the cycle-entry proof relate the initial chain length to the meeting-point distance?

## Python and C++23

C++ uses scalar indices into the referenced vector and never modifies values. Both versions meet the constant-extra-space and input-preservation requirements. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.

# 279 · Perfect Squares

[LeetCode problem](https://leetcode.com/problems/perfect-squares/)

## Intuition
Try which perfect square could be the last summand of an optimal representation.

## Baseline and approach
Breadth-first search through reachable totals is an independent baseline. Increasing-total DP reuses each smaller optimum.

## Why it works
Each valid representation ends in a square q, leaving a representation of total−q. Smaller totals are already optimal, and adding one square to the best predecessor therefore covers all final choices. The zero-total count is zero.

## Complexity
Python: **O(n sqrt(n)) time; O(n) auxiliary space**. n is the target. There are O(sqrt(n)) candidate squares and O(n) DP states; their generated list is included in O(n) auxiliary space.

## Pitfalls
The answer counts squares, not distinct denominations; a square may repeat. Generate squares once, and stop scanning them when they exceed the current total.

## Follow-up
Which number-theoretic tests can decide whether the answer is one, two, three, or four?

## C++23 counterpart
**O(n sqrt(n)) time; O(n) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

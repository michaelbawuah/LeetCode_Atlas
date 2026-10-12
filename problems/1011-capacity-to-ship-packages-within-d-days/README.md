# 1011 · Capacity To Ship Packages Within D Days

[Problem](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) · Medium

## Idea and approaches

Binary-search capacity between the heaviest package and the total weight. Exhaustively trying order-preserving partitions is the baseline; a monotone feasibility check narrows the answer.

## Correctness invariant

For a fixed capacity, filling each day as far as possible cannot use more days than ending it earlier, because it leaves no additional package for future days. The scan therefore finds the minimum days required at that capacity. Larger capacities cannot increase that count. Retaining the feasible upper half or infeasible lower half locates the smallest sufficient capacity.

## Complexity

O(n log S) time for total weight S and O(1) auxiliary space. Input order is preserved; packages cannot be rearranged.

## Verification and pitfalls

The independent oracle enumerates every contiguous partition into at most days groups and minimizes its maximum group weight. Named tests include one day and one package per day.

The lower search bound must include the heaviest indivisible package. Reset the current load when starting a new day.

**Follow-up:** How would the search change if package order could be freely rearranged?

## Python and C++23

C++ reads weights by reference and preserves order. The official n <= 50000 and weight <= 500 bound keeps total weight at most 25000000, safely within int. Both methods use only scalar search and load state. The JSON adapter owns decoded inputs; its conversion copies are outside the solution bounds.

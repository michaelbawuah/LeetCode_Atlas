# 63 · Unique Paths II

[LeetCode problem](https://leetcode.com/problems/unique-paths-ii/)

## Intuition
Count routes from above and from the left, but erase the count whenever the cell is blocked.

## Baseline and approach
Enumerating right/down routes is exponential. A rolling row reuses each smaller cell count once.

## Why it works
Before an open-cell update, paths[column] is the count from above and paths[column−1] is the count from the current row’s left cell. Their routes have different final moves, so counts add. An obstacle contributes zero and prevents all paths through that cell.

## Complexity
Python: **O(r c) arithmetic operations time; O(c) integer states auxiliary space**. r and c are grid dimensions. Python counts O(rc) arithmetic operations and O(c) integer states; intermediate integers may require many bits. C++ adds two capped 64-bit operands, making every addition safe and bounded-width. Neither implementation changes the grid.

## Pitfalls
A blocked finish does not bound the counts in earlier cells. The 40×40 regression has enormous open-prefix counts but answer zero. C++ caps each 64-bit state at 2,000,000,000 before the next addition; addition and resetting to zero commute with saturation. Thus each state equals its true count capped at that limit, and the guaranteed-bounded final answer remains exact.

## Follow-up
How would allowing diagonal movement change the predecessors and storage?

## C++23 counterpart
**O(r c) bounded-width operations time; O(c) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

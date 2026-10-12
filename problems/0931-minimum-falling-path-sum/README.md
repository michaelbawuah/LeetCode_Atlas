# 931 · Minimum Falling Path Sum

[LeetCode problem](https://leetcode.com/problems/minimum-falling-path-sum/)

## Intuition
Each cell can follow one of the three nearby columns in the previous row.

## Baseline and approach
Enumerating falling routes is exponential. A rolling row retains the cheapest prefix cost for each column.

## Why it works
Every route to a cell ends at its above-left, above, or above-right predecessor, so adding the cell value to their minimum gives the optimum. The first row supplies initial single-cell paths; the smallest last-row cost finishes the route.

## Complexity
Python: **O(n²) time; O(n) auxiliary space**. n is square dimension. Python’s temporary predecessor slice contains at most three entries, so it adds O(1) space per update. Old and new rows use O(n) storage; both versions use O(n²) time.

## Pitfalls
Negative cells are legal. Clip predecessor columns at the edges and finish at any bottom-row column. Preserve the input matrix.

## Follow-up
How would the cost change if moves could span an arbitrary column distance?

## C++23 counterpart
**O(n²) time; O(n) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

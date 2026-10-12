# 11 · Container With Most Water

[Problem](https://leetcode.com/problems/container-with-most-water/) · Medium · Two pointers

## Idea

The shorter endpoint determines the water height. Start at maximum width, record
the area, and move an endpoint that currently limits the height.

**Baseline:** evaluate every pair of bars: O(n²) time and O(1) extra space.
**Chosen approach:** use one pointer at each end and move the shorter bar inward.
For `[1, 100, 100, 1]`, the outer pair stores only 3; the inner pair stores 100.

## Why it works

Suppose the left height is no greater than the right height. Any container using
that same left bar and a closer right bar has smaller width and height at most
the left height, so it cannot beat the area already checked. Discarding the left
bar is safe. The argument is symmetric for the right bar. Equal heights allow
either endpoint to be discarded. Taking the maximum of all checked areas therefore
retains an optimum.

## Complexity

O(n) time and O(1) auxiliary space: each step reduces the pointer interval by one.

## Tests and pitfalls

Cover two bars, zero heights, rising heights, equal endpoints, and tall internal
bars. Generated tests compare every pair; a second property checks that multiplying
all heights scales the area equally. Width is `right - left`, and capacity uses
the minimum of the endpoint heights, not their maximum.

**Follow-up:** why does moving the taller endpoint lack the same safe-discard proof?

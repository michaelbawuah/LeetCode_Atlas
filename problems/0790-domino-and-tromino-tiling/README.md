# 790 · Domino and Tromino Tiling

[LeetCode problem](https://leetcode.com/problems/domino-and-tromino-tiling/)

## Intuition
Count complete boards while accounting for the asymmetric gaps introduced by trominos.

## Baseline and approach
A geometry-based four-mask profile model independently counts tile placements. Eliminating the gap states yields the compact recurrence f[n]=2f[n−1]+f[n−3].

## Why it works
A complete final column comes from a vertical domino, a pair of horizontal dominoes, or paired tromino boundaries around a gap region. Tracking the two symmetric gap states gives f[n]=f[n−1]+f[n−2]+2g[n−1] and g[n]=g[n−1]+f[n−2]. Subtracting adjacent equations eliminates g and gives the implemented recurrence, with f[0]=1, f[1]=1, and f[2]=2.

## Complexity
Python: **O(n) time; O(1) auxiliary space**. n is board width. Three rolling counts use O(n) time/O(1) space. The independent oracle builds transitions from actual domino and L-tromino geometry rather than repeating this recurrence.

## Pitfalls
Trominos may rotate. Count entire tilings, not just tile-type counts. Apply the required modulus on every recurrence update.

## Follow-up
How could matrix exponentiation evaluate the recurrence for a much larger n?

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

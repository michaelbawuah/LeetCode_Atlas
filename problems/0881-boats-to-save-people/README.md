# 881 · Boats to Save People

[Problem](https://leetcode.com/problems/boats-to-save-people/) · Medium

## Idea and approaches

Send the heaviest remaining person, pairing with the lightest if possible. Exhaustively enumerating legal pairings is an exponential baseline.

## Correctness invariant

If the lightest cannot share with the heaviest, nobody else can, so the heaviest needs a boat alone. Otherwise an optimum exists pairing them: exchanging partners to make this pair cannot increase boat count because the lightest is no heavier than the replaced partner. Removing that chosen boat preserves an optimal subproblem.

## Complexity

O(n log n) time and O(n) auxiliary space for Python sorting and its copied list. Input is preserved; the return is a scalar boat count.

## Verification and pitfalls

The independent oracle explores all pairings using a memoized subset mask, without a greedy partner rule. Cases cover exact-fit pairs, equal people, and no feasible pairs.

A boat can carry at most two people, regardless of unused weight capacity. Every individual weight is at most limit under the contract.

**Follow-up:** Why does allowing three people per boat destroy this simple pairing argument?

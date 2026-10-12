# 1046. Last Stone Weight

[Problem on LeetCode](https://leetcode.com/problems/last-stone-weight/) · Easy

## Intuition
Each step needs the two largest remaining weights. Negating weights lets Python's min-heap supply them without sorting again.

## Approaches
- **Baseline:** repeatedly sort the remaining stones before each smash: O(n² log n) time in the worst case, O(n) space.
- **Optimized:** build a max-heap representation once, pop two weights, and reinsert their positive difference when unequal.

## Correctness invariant
The heap contains exactly the weights still present in the simulation, with their signs reversed. Its two smallest entries represent the two heaviest stones. Replacing them with their nonzero difference, or with nothing when equal, performs the required smash exactly. Each step decreases the number of remaining stones, so the final empty or single-stone state is the result.

## Complexity
O(n log n) time, including O(n) heap construction and at most n - 1 smash steps. O(n) extra space for the heap copy.

## Edge cases and pitfalls
Equal stones both disappear. Keep the sign convention consistent when reinserting a difference. The returned answer is zero when no stone remains, and the input list is preserved.

## Follow-up
Why does always smashing the two heaviest differ from choosing arbitrary pairs to minimize the final weight?

## Verification
Named fixtures and an independent generated-input reference accompany this implementation. Official judge results are tracked separately in metadata.

# 416 · Partition Equal Subset Sum

[LeetCode problem](https://leetcode.com/problems/partition-equal-subset-sum/)

## Intuition
Equal halves require an even total. Then the question becomes whether any single-use subset reaches half that total.

## Baseline and approach
Enumerating every index subset is exponential. A Boolean table of reachable sums reuses partial results without storing the subsets themselves.

## Why it works
Before processing a number, possible[s] describes reachability using earlier numbers. The update retains an existing witness or extends one totaling s−value. Traversing sums downward ensures that the predecessor still belongs to the previous iteration, so the current number cannot be reused. Reaching half the total leaves its complement with exactly the same sum.

## Complexity
For n numbers and half-total T, **O(nT) time and O(T) auxiliary space**. Python and C++ use the same recurrence and preserve the input. Positive official inputs bound the full total by 20,000.

## Pitfalls
An even total is necessary but insufficient. Ascending updates accidentally implement unlimited reuse. A singleton cannot form two equal halves under the positive-value domain.

## Follow-up
How would recording predecessor choices allow you to return both subsets?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.

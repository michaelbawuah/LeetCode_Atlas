# 15 · 3Sum

[Problem](https://leetcode.com/problems/3sum/) · Medium · Sorting and two pointers

## Idea

After sorting, fix one value and search the remaining suffix for a pair summing
to its negation. Sorted order lets a too-small sum move left upward and a too-large
sum move right downward.

**Baseline:** enumerate all triples of distinct indices and deduplicate their values:
O(n³) time.
**Chosen approach:** sort the values, scan each distinct anchor, and use two pointers.
Python sorts a copy; C++ sorts the supplied vector in place.
After a match, skip repeated partner values so each value triple appears once.

## Why it works

For a fixed anchor, if the sum is too small, every remaining pair using the current
left endpoint has an equal or smaller sum, so that endpoint can be discarded.
The symmetric argument discards a right endpoint when the sum is too large.
Thus no potential match is skipped. Equal anchors have identical suffix-value
possibilities; skipping them and repeated partners prevents duplicate triples.

## Complexity

O(n²) time: O(n log n) sorting plus O(n) work for each anchor. O(n) auxiliary
space for the sorted copy and Python's sort workspace, excluding the result.
There can be O(n²) unique result triples.

The C++ version also takes O(n²) time. It avoids a full input copy; a typical
`std::sort` implementation uses O(log n) auxiliary stack space, excluding output.

## Tests and pitfalls

Cases exercise repeated zeroes, repeated partners, no solution, and multiple triples.
Generated tests enumerate combinations of three distinct positions and deduplicate
their sorted values. A set of input values would be wrong because multiplicity matters.
Python preserves the caller's array by sorting a copy. C++ changes its input
order by sorting the supplied vector. The local adapter gives each call its own
input vector, so this mutation cannot leak into a later shared case.
The shared checker permits arbitrary order both between and within triples,
while retaining multiplicity to reject duplicated result triples.

**Follow-up:** how would you generalize the recursion to k-sum while pruning impossible ranges?

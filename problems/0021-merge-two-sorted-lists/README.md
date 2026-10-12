# 21 · Merge Two Sorted Lists

[LeetCode problem](https://leetcode.com/problems/merge-two-sorted-lists/)

## Intuition
The smallest remaining value must be at the head of one of the two sorted lists.

## Baseline and approach
Collecting every value and sorting them costs O((m+n) log(m+n)) time and O(m+n) space. Two pointers append the smaller head node to a result tail, then advance just that input. A dummy node simplifies the first append. Once an input is exhausted, attach the other's already sorted suffix.

## Why it works
The result prefix is sorted and contains exactly the nodes consumed so far. Choosing the smaller remaining head appends the smallest unconsumed value, preserving sorted order. The untouched suffix is sorted and cannot be smaller than the last appended value, so attaching it completes the merge.

## Complexity
For input lengths m and n: **O(m+n) worst-case time, O(1) auxiliary space**. Existing nodes are reused; one dummy node is allocated.

## Pitfalls
Attach the leftover suffix after the loop. Equal values must both survive. This implementation changes the input links, so callers needing original lists should copy them first.

## Follow-up
For k sorted lists, compare repeatedly merging pairs with maintaining a heap of current heads.

## Python and C++23
Both versions reuse and relink the input nodes, allocating only a dummy predecessor. The C++ adapter retains ownership of both input lists through one ListArena, so merging does not transfer or duplicate node ownership.

C++23 submission-method complexity: **O(m + n) time; O(1) space**. Adapter ownership and JSON conversion costs are separate.

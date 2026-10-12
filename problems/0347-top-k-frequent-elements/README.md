# 347 · Top K Frequent Elements

[Problem](https://leetcode.com/problems/top-k-frequent-elements/) · Medium · Buckets

## Idea

Each frequency is between 1 and the input length, so frequencies themselves can
index buckets. Visit high-frequency buckets first.

**Baseline:** count values and sort all distinct values by frequency:
O(n + u log u) expected time for u distinct values.
**Chosen approach:** count once, place each distinct value in its frequency bucket,
then collect from largest frequency downward until k values have been selected.

## Why it works

Every distinct value enters exactly one bucket matching its occurrence count.
The descending scan considers every greater frequency before any smaller one.
The first k values therefore form the top-k set. The problem guarantees a unique
answer, so a tie cannot straddle the selected-set boundary.

## Complexity

O(n) expected time and O(n) auxiliary space. Counting assumes expected constant-time
hash operations; bucket construction and scanning are linear. A heap can use less
bucket memory when k is small, at the cost of O(u log k) selection time.

## Tests and pitfalls

Test k = 1, selecting every distinct value, negative values, zero, and ties entirely
inside the selected set. Generated tests compare against full sorting with distinct
frequencies. Output order is irrelevant; output length and uniqueness still matter.

**Follow-up:** how would you maintain top-k values in an unbounded stream?

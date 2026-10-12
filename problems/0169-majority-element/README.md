# 169 · Majority Element

[Problem](https://leetcode.com/problems/majority-element/) · Easy · Boyer–Moore voting

## Approach

**Baseline:** count every value in a frequency map, taking O(n) extra space.
**Chosen approach:** keep one candidate and a vote balance. Equal values add a
vote; different values cancel one. A zero balance lets the next value become candidate.

## Invariant and correctness

The processed values can be viewed as a collection of removed unequal pairs
plus the remaining copies of the current candidate represented by its balance.
Removing an unequal pair cannot eliminate the strict-majority property of the
original majority among remaining values. Since a majority is guaranteed to exist,
it must be the final surviving candidate.

## Complexity and languages

Both implementations use O(n) time and O(1) auxiliary space, returning a scalar.
Neither mutates input, and C++ accepts the vector by reference rather than copying it.
Votes are bounded by the input length and fit the C++ `int` type.

## Verification and pitfalls

Generated arrays contain a guaranteed majority and are permuted before testing.
The independent oracle reads the sorting median. Fixtures include zero, negative,
singleton, and changing candidates. If a majority were not guaranteed, a second
counting pass would be necessary to validate the surviving candidate.

**Follow-up:** how does candidate cancellation extend to values occurring more than n/3 times?

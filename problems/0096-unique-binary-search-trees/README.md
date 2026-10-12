# 96 · Unique Binary Search Trees

[LeetCode problem](https://leetcode.com/problems/unique-binary-search-trees/)

## Intuition
Choosing a root determines how many smaller keys lie on the left and larger keys on the right.

## Baseline and approach
Explicitly constructing all BST shapes is exponential. Count shapes by node count, multiplying independent left and right possibilities for each root.

## Why it works
For a tree of size s, a root choice partitions the ordered keys into l left keys and s−1−l right keys. Every pair of subtree shapes yields one distinct tree, and different roots are disjoint cases. Summing these products gives the total. One empty subtree shape supplies counts[0]=1.

## Complexity
Python: **O(n²) time; O(n) auxiliary space**. n≤19 bounds the final Catalan number within signed 32-bit range. Python and C++ use O(n) states; C++ performs widened products before the final int conversion.

## Pitfalls
The empty subtree count is one, even though public inputs start at one. C++ operands are int64_t before multiplication and accumulation; converting a narrow overflowing product afterward would be too late.

## Follow-up
How can the Catalan closed form compute the same count without a quadratic table?

## C++23 counterpart
**O(n²) time; O(n) auxiliary space**. The implementation uses the same recurrence and preserves its inputs. JSON adaptation costs are separate from the submission method.

## Verification
Named fixtures and an independent generated-input oracle accompany this implementation. Official judge results are recorded separately in metadata.

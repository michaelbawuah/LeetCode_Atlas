# 58. Length of Last Word

[Problem on LeetCode](https://leetcode.com/problems/length-of-last-word/) · Easy

## Approach

Splitting the string stores every word. Scan backward past trailing spaces and then count the final word.

## Invariant and correctness

After skipping spaces, end marks the final word character. Moving left until a separator or the beginning visits exactly that word; end minus the stopping index is its length.

## Complexity

Time: O(n). Space: O(1).

## Boundaries and pitfalls

The contract guarantees at least one word, with English letters and spaces. The initial space-skipping loop relies on that guarantee.

## Follow-up

Find the lengths of the last k words with one backward scan.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp) · [Parity generator](parity.py)

Both versions preserve input unless the problem specifies mutation. C++ string arguments use const references; adapter-decoded inputs are separately owned and excluded from solution auxiliary space.

Time: O(n). Space: O(1).

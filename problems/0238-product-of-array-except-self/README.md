# 238 · Product of Array Except Self

[Problem](https://leetcode.com/problems/product-of-array-except-self/) · Medium · Prefix/suffix

## Idea

Everything except index i is the product strictly to its left multiplied by the
product strictly to its right. Neither division nor special zero handling is needed.

**Baseline:** multiply all other values separately for each index: O(n²) time.
**Chosen approach:** write exclusive prefix products into the output, then multiply
them by a rolling exclusive suffix product in a reverse pass.

For `[2, 3, 4]`, the prefix pass writes `[1, 2, 6]`; suffix multipliers
`[12, 4, 1]` produce `[12, 8, 6]`.

## Why it works

Before the first pass processes i, `prefix` equals the product of indices less
than i. Before the reverse pass processes i, `suffix` equals the product of
indices greater than i. Their product excludes exactly the current element.

## Complexity

O(n) time and O(1) auxiliary space excluding the required O(n) output array, under
the bounded-integer arithmetic model of the problem. Python integers avoid fixed-width
overflow; very large unrestricted integers would add arithmetic bit complexity.

## Tests and pitfalls

Cases cover no zeroes, one zero, two zeroes, negative factors, and arrays of length
two. The independent oracle multiplies a sliced list excluding each index.
Update each running product after using it, or the current element leaks into its
own answer. Multiplicative identity is 1, not 0.

**Follow-up:** how does the same technique apply to sums or other associative operations?

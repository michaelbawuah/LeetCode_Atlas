# 394. Decode String

[Problem on LeetCode](https://leetcode.com/problems/decode-string/) · Medium

## Approach

Repeatedly locating innermost bracket groups rescans the input. A stack retains each enclosing prefix and multiplier while decoding its child.

## Invariant and correctness

pieces holds decoded fragments of the current bracket level. A closing bracket joins exactly that level, repeats it, and appends it to its saved parent. Valid nesting restores the correct parent at every close.

## Complexity

Time: O(n + Ld), decoded length L and nesting depth d. Space: O(n + L).

## Boundaries and pitfalls

Account for expanded output and repeated copying across depth, not just encoded length. The input is valid, counts positive, and literal text lowercase.

## Follow-up

Emit decoded characters lazily without materializing the entire expansion.

## Verification

Named cases and an independent generated-input oracle or operation model accompany the source. Judge results are recorded separately in metadata.

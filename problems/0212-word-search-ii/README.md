# 212. Word Search II

[Problem on LeetCode](https://leetcode.com/problems/word-search-ii/) · Hard

## Approach, invariant, and complexity

Store the dictionary in a trie, then search board paths only while their letters remain a dictionary prefix. Remove a terminal marker after finding its word so several board paths cannot emit duplicates.

A baseline independently searches the board for each word. The trie shares prefix exploration. In a recursive call, its node corresponds exactly to the active board path. Compatible unused neighbors extend that prefix, while a terminal marker proves a complete word. Removing an exhausted trie branch is safe because it contains no undiscovered words. Restore marked cells on return.

For total dictionary characters T and maximum word length L, a conservative bound is O(T + mn × 4^L) time. Trie and active-path storage cost O(T + L); output references cost O(K) for K found words. Pruning often reduces work, but it does not remove the exponential worst case.

Different board paths may spell the same word; return it once. A word may be a prefix of another, so finding its terminal does not discard its remaining children. Input words are distinct lowercase strings, and the board is preserved.

Follow-up: return a path for each found word rather than only its name. Which path state must be copied when recording an answer?

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

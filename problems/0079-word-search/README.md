# 79. Word Search

[Problem on LeetCode](https://leetcode.com/problems/word-search/) · Medium

## Approach, invariant, and complexity

Try each cell as a starting point and extend only along neighbors matching the next letter. Temporarily mark the active path so a cell cannot be reused.

A baseline enumerates every simple path before checking its letters. Prefix checks prune incompatible paths immediately. During recursion the marked cells are exactly the chosen path; each call adds a matching adjacent unused cell. Reaching the final character proves a valid path. Exhausting every compatible extension from every start proves absence.

The conservative bound is O(mn × 4^L) time for an m-by-n board and word length L; excluding the immediate predecessor tightens the branching after the first move. Auxiliary recursion space is O(L). The board is restored before returning, including after successful searches.

Diagonal movement is forbidden. Equal letters on different cells are allowed, but one cell cannot serve two positions in the same word. Reject words longer than the number of cells.

Follow-up: search many words together. How does a trie avoid repeating work for shared prefixes?

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

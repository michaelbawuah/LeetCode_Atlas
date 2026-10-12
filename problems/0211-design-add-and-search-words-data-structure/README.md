# 211. Design Add and Search Words Data Structure

[Problem on LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/) · Medium

## Intuition
A literal follows one trie edge. A dot may follow every child edge, so the search keeps all nodes compatible with the pattern prefix.

## Approaches
- **Baseline:** store words in a set and test every same-length candidate against the query: O(WL) query time for W words and length L.
- **Optimized:** insert words into a trie and advance a frontier of compatible nodes for each pattern character.

## Correctness invariant
After processing the first i query characters, the frontier contains exactly the trie nodes whose root paths match that length-i prefix. A literal keeps the matching child from each node; a dot keeps all children. If the frontier becomes empty, no word can match. At the end, a terminal node proves a complete stored word matches, rather than only a prefix.

## Complexity
Insertion takes O(L) expected time for dictionary lookups. A search takes O(min(N, L × 26^w)) time, where N is the number of trie nodes and w is the number of dots in a length-L query: only compatible nodes are visited, and each visited node has a unique root path. Search frontier space is O(min(N, 26^w)). Stored trie space is O(T) for total inserted character count T. The alphabet is fixed to lowercase English letters.

## Edge cases and pitfalls
A dot matches exactly one character. A valid matching prefix without a terminal flag is insufficient. Duplicate additions do not create duplicate paths. Test sequences use nonempty words and queries with at most two dots, including queries before any word is inserted.

## Follow-up
Add a wildcard that matches zero or more characters. What additional search state would prevent repeated work?

## Verification
Named fixtures and an independent generated-input reference accompany this implementation. Official judge results are tracked separately in metadata.

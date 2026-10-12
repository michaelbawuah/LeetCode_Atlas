# 139 · Word Break

[LeetCode problem](https://leetcode.com/problems/word-break/)

## Intuition
A valid segmented prefix ends with a dictionary word whose preceding prefix was also segmentable.

## Baseline and approach
Enumerating all cut positions is exponential. Prefix reachability tests only lengths that occur in the dictionary, avoiding impossible candidate lengths.

## Why it works
Before computing possible[end], every shorter prefix has its correct reachability. A successful length provides a reachable preceding prefix and a dictionary suffix, establishing a segmentation. Conversely every segmentation has one such last word, so trying all dictionary lengths covers every witness.

## Complexity
Let n be string length, W dictionary size, T total dictionary characters, and L maximum dictionary word length. **O(T + nL²) expected time** includes substring copying and hashing. Python auxiliary space is **O(W+n+L)**: its set references existing word strings. C++ copies words into its set and uses **O(T+n+L)** space. Neither changes the inputs.

## Pitfalls
The same dictionary word may be reused. Greedy longest-prefix selection can miss a valid shorter split, as in cars with car, ca, and rs. Treating each substring lookup as O(1) would omit copying and hashing costs.

## Follow-up
How would a trie avoid creating a temporary substring for every dictionary-length lookup?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.

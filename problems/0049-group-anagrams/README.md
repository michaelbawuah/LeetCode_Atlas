# 49 · Group Anagrams

[Problem](https://leetcode.com/problems/group-anagrams/) · Medium · Hash map

## Idea

Assign each word a signature that ignores order but preserves multiplicity.
Words sharing a signature belong to the same group.

**Baseline:** compare each word against group representatives, with repeated
character comparisons. A simpler improved baseline uses sorted words as keys,
costing O(Σ |word| log |word|).
**Python approach:** use a 26-entry frequency tuple as a dictionary key.
`"eat"`, `"tea"`, and `"ate"` produce the same tuple.

**C++ approach:** sort a copy of each word and use that string as the hash key.
The sorted key also preserves letter multiplicities, and avoids requiring a
custom hash for a fixed-size frequency array.

## Why it works

For lowercase English letters, two frequency tuples are equal exactly when every
letter has the same multiplicity. Sorted keys are equal under exactly the same
condition. That is precisely the anagram relation. Each input word is appended
once to its signature's group, preserving repeated words.

## Complexity

For Python, let N be the number of words and L their total character count. Expected time is
O(N + L): each word initializes a constant-size tuple and each character is counted
once. Additional space is O(N) for constant-size signatures and word references.
The strings themselves are reused rather than copied.

C++ takes expected O(N + Σ |word| log(|word| + 1)) time, including sorting and
hashing keys. Its stored keys and copied output strings take O(N + L) space.
This difference is recorded separately in metadata rather than assigning the
Python frequency-counting bound to both implementations.

## Tests and pitfalls

Cases include empty strings, repeated words, and different word lengths. Generated
tests group by sorted characters and separately check the multiset of output words.
Group order and within-group order are irrelevant, but duplicates must be retained.
The 26-slot implementation relies on the lowercase-English input constraint.

**Follow-up:** for an unrestricted alphabet, which signature would you choose?

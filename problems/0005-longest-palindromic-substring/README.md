# 5 · Longest Palindromic Substring

[LeetCode problem](https://leetcode.com/problems/longest-palindromic-substring/)

## Intuition
Expand outward from each character and each gap. A palindrome always has one of these odd or even centers.

## Baseline and approach
Testing every slice by reversing it costs O(n³). Center expansion checks matching boundary pairs directly, retaining indices for the longest interval instead of copying each candidate.

## Why it works
At every successful expansion, the current interval is palindromic: its interior was already a palindrome and the two new boundary characters match. Expansion stops precisely when that center cannot extend. Every palindromic substring has one enumerated center, so comparing the maximal expansions finds the global maximum.

## Complexity
For length n, **O(n²) time and O(1) auxiliary space**. The final returned slice occupies O(n) space in the worst case.

## Pitfalls
Even palindromes use a gap center. More than one maximum substring can be valid, so the semantic checker verifies membership, symmetry, and maximum length rather than requiring a particular witness. Characters are case sensitive; digits are valid input.

## Follow-up
How would Manacher’s algorithm reuse information across neighboring centers to obtain linear time?

## Verification
Named fixtures and independent generated-input references accompany the implementation. Official judge results are tracked separately in metadata.

## C++23 counterpart

The submission method takes a string by value, so the input copy costs O(n) storage; the center-expansion core retains only indices, and the final substring owns its output. The semantic checker accepts every longest palindromic witness rather than imposing a tie choice. Signed boundary indices are checked before conversion to size_t.

C++: **O(n² + n) time; O(n) input copy and output; O(1) core auxiliary space**. Named fixtures and 150 reproducible generated inputs compare this implementation with the Python track.

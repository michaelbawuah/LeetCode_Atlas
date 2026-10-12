# 71. Simplify Path

[Problem on LeetCode](https://leetcode.com/problems/simplify-path/) · Medium

## Approach, invariant, and complexity

Scan path components while retaining the directories of the current canonical absolute path. Ignore empty components and dot; dot-dot removes the current final directory if one exists.

A baseline repeatedly rewrites dot segments and separators in the string, potentially O(L²) time. The stack describes the normalized path after every processed component. A name descends one level, dot stays in place, and dot-dot ascends at most to root. Joining this final stack therefore produces exactly the canonical path.

Time and extra space are O(L) for input length L, including split components and the returned string. This is lexical path normalization; it does not resolve filesystem symbolic links.

Only exactly dot and dot-dot have special meaning. Names such as three dots or dot-prefixed files are ordinary directories. Repeated separators and attempts to ascend above root must collapse correctly.

Follow-up: resolve symbolic links with a supplied link map while detecting cycles.

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

## C++23 counterpart

[Source](solution.cpp) · [Local adapter](cpp_runner.cpp)

The C++ implementation tokenizes with a string stream and stores copied components. String copies and output construction are included in its O(L) memory and amortized time bounds.

Time: O(L) amortized. Space: O(L). The local adapter constructs a fresh object for each fixture and owns any converted inputs.

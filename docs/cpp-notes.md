# Python and C++23 notes

[Problem catalog](problems.md) · [Verification](verification.md) · [Repository](../README.md)

Both language tracks solve the same problems and share named fixtures. Their representations can differ: Group Anagrams uses frequency tuples in Python and sorted-string keys in C++. Python emphasizes a readable problem-solving path; C++23 adds attention to value ranges, references, containers, and pointer behavior.

## Current counterparts

| Problem | Python | C++23 | Comparison to examine |
|---|---|---|---|
| [Two Sum](../problems/0001-two-sum/README.md) | [Source](../problems/0001-two-sum/solution.py) | [Source](../problems/0001-two-sum/solution.cpp) | Dictionary and unordered-map lookup; complement arithmetic |
| [Longest Substring](../problems/0003-longest-substring-without-repeating-characters/README.md) | [Source](../problems/0003-longest-substring-without-repeating-characters/solution.py) | [Source](../problems/0003-longest-substring-without-repeating-characters/solution.cpp) | Character keys and index representations |
| [3Sum](../problems/0015-3sum/README.md) | [Source](../problems/0015-3sum/solution.py) | [Source](../problems/0015-3sum/solution.cpp) | Sorting, copies, and integer promotion |
| [Valid Parentheses](../problems/0020-valid-parentheses/README.md) | [Source](../problems/0020-valid-parentheses/solution.py) | [Source](../problems/0020-valid-parentheses/solution.cpp) | List and vector stack operations |
| [Rotated Array Search](../problems/0033-search-in-rotated-sorted-array/README.md) | [Source](../problems/0033-search-in-rotated-sorted-array/solution.py) | [Source](../problems/0033-search-in-rotated-sorted-array/solution.cpp) | Inclusive Python interval and half-open C++ interval |
| [Group Anagrams](../problems/0049-group-anagrams/README.md) | [Source](../problems/0049-group-anagrams/solution.py) | [Source](../problems/0049-group-anagrams/solution.cpp) | Immutable signatures and hashing |
| [House Robber](../problems/0198-house-robber/README.md) | [Source](../problems/0198-house-robber/solution.py) | [Source](../problems/0198-house-robber/solution.cpp) | Updating compressed state without losing old values |
| [Reverse Linked List](../problems/0206-reverse-linked-list/README.md) | [Source](../problems/0206-reverse-linked-list/solution.py) | [Source](../problems/0206-reverse-linked-list/solution.cpp) | References, raw pointers, and node lifetime |
| [Product Except Self](../problems/0238-product-of-array-except-self/README.md) | [Source](../problems/0238-product-of-array-except-self/solution.py) | [Source](../problems/0238-product-of-array-except-self/solution.cpp) | Intermediate products and fixed-width arithmetic |
| [Daily Temperatures](../problems/0739-daily-temperatures/README.md) | [Source](../problems/0739-daily-temperatures/solution.py) | [Source](../problems/0739-daily-temperatures/solution.cpp) | Index stacks, strict comparisons, and distance types |

## Numeric types

Python integers grow as needed; C++ integer types have fixed bounds. Check intermediate expressions as well as final results. Cast before arithmetic when a wider type is required: widening the result after an overflow has already happened cannot repair it.

Complexity notes commonly treat bounded integer operations as constant time. That assumption follows the problem's constraints; it does not mean arbitrary-precision arithmetic is always constant time.

## Collections and ordering

Dictionary and unordered-map operations have expected constant-time behavior. Their iteration order need not define the answer's order. For problems that permit arbitrary grouping or tuple order, shared fixtures use the problem's checker to compare meaning rather than incidental ordering.

Sorted copies consume memory. A Python slice also allocates a new list, even when it appears only in a loop header. In C++, passing a vector by reference avoids a parameter copy, but sorting that reference changes the input unless a local copy is made.

## Indexes and pointers

Keep a consistent interval convention in binary search. Rotated-array search uses `[left, right]` in Python and unsigned indexes with `[left, end)` in C++; the latter allows `end = middle` without subtracting from an unsigned zero. Compute the middle from the interval width rather than adding endpoints unnecessarily.

In linked-list code, save `next` before overwriting a link. The problem supplies the node type; local adapters supply a compatible type for tests. Reversing links does not require allocating replacement nodes. The test harness owns and cleans up its allocated nodes.

## Submission code and local adapters

`solution.py` and `solution.cpp` retain the expected LeetCode class and method interface. A `cpp_runner.cpp` adapts JSON fixtures to that interface for local execution. Lists and trees are built by the harness where needed; adapter details stay outside submission code.

The local build requests C++23. These foundation algorithms use familiar STL containers and loops, so their explanations focus on algorithmic choices rather than demonstrating new language syntax.

## Build and compare

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --parallel
ctest --test-dir build --output-on-failure
ATLAS_CPP_BIN_DIR=build/bin python -m pytest tests/test_cases.py
ATLAS_CPP_BIN_DIR=build/bin python -m pytest tests/test_cpp_properties.py
```

The last two commands include the compiled implementations in shared-fixture checks and generated-input comparisons. Agreement between languages is useful evidence, but both implementations could share the same mistake. Independent property oracles provide a separate line of verification.

See [verification](verification.md) for sanitizer checks and the distinction between local checks and official judge results.

# Python and C++23 notes

[Problem catalog](problems.md) · [Verification](verification.md) · [Repository](../README.md)

The 25 C++23 counterparts share named fixtures with Python, plus 150 generated comparisons per counterpart. Different representations and algorithms make the comparison useful: Python favors an explicit problem-solving path, while C++ makes fixed-width arithmetic, references, container operations, and node lifetime visible.

## Current counterparts

| Problem | Python | C++23 | Comparison to examine |
|---|---|---|---|
| [Two Sum](../problems/0001-two-sum/README.md) | [Source](../problems/0001-two-sum/solution.py) | [Source](../problems/0001-two-sum/solution.cpp) | Dictionary and unordered-map lookup; widened complement subtraction |
| [Longest Substring](../problems/0003-longest-substring-without-repeating-characters/README.md) | [Source](../problems/0003-longest-substring-without-repeating-characters/solution.py) | [Source](../problems/0003-longest-substring-without-repeating-characters/solution.cpp) | Character map versus a fixed byte-index table |
| [3Sum](../problems/0015-3sum/README.md) | [Source](../problems/0015-3sum/solution.py) | [Source](../problems/0015-3sum/solution.cpp) | Sorting, duplicate skips, and widened sum arithmetic |
| [Remove Nth Node](../problems/0019-remove-nth-node-from-end-of-list/README.md) | [Source](../problems/0019-remove-nth-node-from-end-of-list/solution.py) | [Source](../problems/0019-remove-nth-node-from-end-of-list/solution.cpp) | Dummy heads and a fixed pointer gap; detach borrowed nodes without deleting them |
| [Valid Parentheses](../problems/0020-valid-parentheses/README.md) | [Source](../problems/0020-valid-parentheses/solution.py) | [Source](../problems/0020-valid-parentheses/solution.cpp) | List and vector stack operations |
| [Rotated Array Search](../problems/0033-search-in-rotated-sorted-array/README.md) | [Source](../problems/0033-search-in-rotated-sorted-array/solution.py) | [Source](../problems/0033-search-in-rotated-sorted-array/solution.cpp) | Inclusive Python bounds and half-open unsigned C++ bounds |
| [Group Anagrams](../problems/0049-group-anagrams/README.md) | [Source](../problems/0049-group-anagrams/solution.py) | [Source](../problems/0049-group-anagrams/solution.cpp) | Python frequency tuples versus C++ sorted-string signatures |
| [Maximum Subarray](../problems/0053-maximum-subarray/README.md) | [Source](../problems/0053-maximum-subarray/solution.py) | [Source](../problems/0053-maximum-subarray/solution.cpp) | Compressed DP and widened intermediate sums |
| [Merge Intervals](../problems/0056-merge-intervals/README.md) | [Source](../problems/0056-merge-intervals/solution.py) | [Source](../problems/0056-merge-intervals/solution.cpp) | Python sorts a copy; C++ sorts the supplied vector in place |
| [Insert Interval](../problems/0057-insert-interval/README.md) | [Source](../problems/0057-insert-interval/solution.py) | [Source](../problems/0057-insert-interval/solution.cpp) | Linear region scans and copied output ranges; input ranges stay intact |
| [Minimum Window](../problems/0076-minimum-window-substring/README.md) | [Source](../problems/0076-minimum-window-substring/solution.py) | [Source](../problems/0076-minimum-window-substring/solution.cpp) | Counter entries versus a fixed byte-count table; count occurrences rather than distinct letters |
| [Validate BST](../problems/0098-validate-binary-search-tree/README.md) | [Source](../problems/0098-validate-binary-search-tree/solution.py) | [Source](../problems/0098-validate-binary-search-tree/solution.cpp) | Explicit inorder stacks; separate previous-value presence from its value |
| [Longest Consecutive Sequence](../problems/0128-longest-consecutive-sequence/README.md) | [Source](../problems/0128-longest-consecutive-sequence/solution.py) | [Source](../problems/0128-longest-consecutive-sequence/solution.cpp) | Hash-set boundary checks and guards at C++ integer limits |
| [Reverse Polish Notation](../problems/0150-evaluate-reverse-polish-notation/README.md) | [Source](../problems/0150-evaluate-reverse-polish-notation/solution.py) | [Source](../problems/0150-evaluate-reverse-polish-notation/solution.cpp) | Truncation toward zero; preserve left/right operand order |
| [House Robber](../problems/0198-house-robber/README.md) | [Source](../problems/0198-house-robber/solution.py) | [Source](../problems/0198-house-robber/solution.cpp) | Update compressed state without losing the older value |
| [Reverse Linked List](../problems/0206-reverse-linked-list/README.md) | [Source](../problems/0206-reverse-linked-list/solution.py) | [Source](../problems/0206-reverse-linked-list/solution.cpp) | Rewire existing nodes while preserving ownership in the adapter |
| [Course Schedule](../problems/0207-course-schedule/README.md) | [Source](../problems/0207-course-schedule/solution.py) | [Source](../problems/0207-course-schedule/solution.cpp) | Adjacency storage, indegrees, and queue-based dependency removal |
| [Kth Largest](../problems/0215-kth-largest-element-in-an-array/README.md) | [Source](../problems/0215-kth-largest-element-in-an-array/solution.py) | [Source](../problems/0215-kth-largest-element-in-an-array/solution.cpp) | Python retains a size-k heap; C++ partitions with nth_element |
| [Product Except Self](../problems/0238-product-of-array-except-self/README.md) | [Source](../problems/0238-product-of-array-except-self/solution.py) | [Source](../problems/0238-product-of-array-except-self/solution.cpp) | Prefix/suffix passes and fixed-width intermediate products |
| [Longest Increasing Subsequence](../problems/0300-longest-increasing-subsequence/README.md) | [Source](../problems/0300-longest-increasing-subsequence/solution.py) | [Source](../problems/0300-longest-increasing-subsequence/solution.cpp) | bisect_left and lower_bound maintain minimum possible tails |
| [Coin Change](../problems/0322-coin-change/README.md) | [Source](../problems/0322-coin-change/solution.py) | [Source](../problems/0322-coin-change/solution.cpp) | Amount-indexed tables and an explicit unreachable state |
| [Redundant Connection](../problems/0684-redundant-connection/README.md) | [Source](../problems/0684-redundant-connection/solution.py) | [Source](../problems/0684-redundant-connection/solution.cpp) | Union by size and path halving over indexed parent arrays |
| [Daily Temperatures](../problems/0739-daily-temperatures/README.md) | [Source](../problems/0739-daily-temperatures/solution.py) | [Source](../problems/0739-daily-temperatures/solution.cpp) | Index stacks, strict comparisons, and distance types |
| [Koko Eating Bananas](../problems/0875-koko-eating-bananas/README.md) | [Source](../problems/0875-koko-eating-bananas/solution.py) | [Source](../problems/0875-koko-eating-bananas/solution.cpp) | Monotone feasibility and widened ceiling-division arithmetic |
| [Rotting Oranges](../problems/0994-rotting-oranges/README.md) | [Source](../problems/0994-rotting-oranges/solution.py) | [Source](../problems/0994-rotting-oranges/solution.cpp) | Multi-source BFS layers; grid updates mark discovered cells |

## Algorithms can differ

For [Kth Largest](../problems/0215-kth-largest-element-in-an-array/README.md), Python keeps the k largest values in a min-heap, using O(n log(k+1)) time and O(k) auxiliary storage. C++ uses `std::nth_element` with descending comparison and changes the input order. Its comparison complexity is linear on average; it has no standard worst-case linear guarantee. The same answer does not imply the same complexity or mutation behavior.

[Group Anagrams](../problems/0049-group-anagrams/README.md) also differs: Python counts a fixed alphabet, while C++ sorts each word's copied signature. Include that per-word sorting cost when analyzing the C++ implementation.

## Numeric types and characters

Python integers grow as needed; C++ integer types have fixed bounds. Check intermediate expressions as well as final results. Cast before arithmetic when widening is needed: widening after overflow cannot repair it. Koko's accumulated hours and ceiling numerator use wider arithmetic; longest-consecutive scanning guards the minimum and maximum `int` boundaries.

Python `//` rounds down, while C++ integer division truncates toward zero. The Python RPN implementation divides absolute values and restores the sign to match the required rule. The C++ implementation uses widened operands and validates its bounded intermediate results.

The C++ substring implementations index fixed tables through `unsigned char`, preventing a signed byte from becoming a negative index. Those tables operate on bytes; they are not Unicode code-point dictionaries.

## Collections, ordering, and mutation

Hash-table costs are generally expected rather than worst-case constant time. Iteration order should only affect the answer when the problem requires it. Declared checkers preserve multiplicity and only remove ordering distinctions that the problem permits.

Python's Merge Intervals uses `sorted(intervals)` and builds fresh result ranges. C++ sorts the input vector and builds a result vector. C++ Insert Interval instead keeps input ranges intact. Slices and sorted copies allocate storage; passing a C++ vector by reference avoids a parameter copy but permits mutation.

Binary search needs a consistent interval convention. Rotated-array search uses `[left, right]` in Python and `[left, end)` with unsigned indexes in C++; half-open bounds avoid subtracting from unsigned zero.

## Node ownership and local adapters

`solution.py` and `solution.cpp` retain LeetCode's class and method interfaces. The platform supplies node types; local adapters supply compatible definitions and construct nodes from JSON fixtures.

C++ [ListArena and TreeArena](../cpp/atlas_adapter.hpp) own nodes through `unique_ptr` storage. Submission methods receive borrowed raw pointers. Reverse Linked List rewires links; Remove Nth Node detaches a node without deleting it. Arena cleanup remains valid even when a node is no longer reachable from the returned head. Moving the owning pointers does not move the nodes themselves.

Trees use queue-based level-order encoding with `null` child positions. `[1,null,2,3]` means that 3 is the left child of 2, not an array-heap index. Serializers trim trailing nulls and reject cycles or shared-child structures. The C++ BST counterpart walks inorder with an explicit stack, taking O(n) time and O(h) auxiliary space.

The Python adapter copies JSON inputs before constructing nodes or passing mutable values. For [Reorder List](../problems/0143-reorder-list/README.md) and [Move Zeroes](../problems/0283-move-zeroes/README.md), `result_from_arg: 0` selects the mutated first argument after the method returns `None`. Submission signatures remain unchanged.

## Build and compare

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --parallel
ctest --test-dir build --output-on-failure
ATLAS_CPP_BIN_DIR=build/bin python -m pytest tests/test_cases.py tests/test_cpp_properties.py
```

The shared-fixture suite requires every configured counterpart runner. The generated suite includes 3,750 comparisons across 25 counterparts. Independent Python oracles provide another verification path because two language implementations can share the same algorithmic mistake.

See [verification](verification.md) for sanitizer settings, recorded command results, and the distinction between local checks and official judge evidence.

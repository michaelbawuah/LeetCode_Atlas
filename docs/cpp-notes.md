# Python and C++23 notes

[Problem catalog](problems.md) · [Verification](verification.md) · [Repository](../README.md)

The 150 C++23 counterparts share named fixtures with Python, plus 150 generated comparisons per counterpart. Different representations and algorithms make the comparison useful: Python favors an explicit problem-solving path, while C++ makes fixed-width arithmetic, references, container operations, and node lifetime visible.

## Selected comparisons

The [full catalog](problems.md) identifies all 150 counterparts. These entries illustrate recurring language choices.

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

[Coin Change II](../problems/0518-coin-change-ii/README.md) has a subtle numeric boundary: its final answer fits a signed 32-bit integer, but other subtotal counts can exceed 64 bits. Python keeps arbitrary-precision counts. C++ widens each addition and saturates nonnegative counts at `INT_MAX`; because no transition subtracts, this preserves the guaranteed-bounded final answer. A named fixture uses an odd target with many even denominations: the answer is zero while unrelated even-subtotal counts grow large.

[Unique Paths II](../problems/0063-unique-paths-ii/README.md) has a related numeric boundary: a blocked destination can keep the final count small while earlier open regions accumulate enormous counts. A nonnegative saturated recurrence preserves the guaranteed-bounded final answer; obstacle cells reset their counts to zero. [Reverse Integer](../problems/0007-reverse-integer/README.md) instead checks the permitted range before returning an accumulated reversed value.

## Collections, ordering, and mutation

Hash-table costs are generally expected rather than worst-case constant time. Iteration order should only affect the answer when the problem requires it. Declared checkers preserve multiplicity and only remove ordering distinctions that the problem permits.

Python's Merge Intervals uses `sorted(intervals)` and builds fresh result ranges. C++ sorts the input vector and builds a result vector. C++ Insert Interval instead keeps input ranges intact. Slices and sorted copies allocate storage; passing a C++ vector by reference avoids a parameter copy but permits mutation.

Binary search needs a consistent interval convention. Rotated-array search uses `[left, right]` in Python and `[left, end)` with unsigned indexes in C++; half-open bounds avoid subtracting from unsigned zero.

## Stateful structures and frontiers

| Problem | Representation and invariant |
|---|---|
| [LRU Cache](../problems/0146-lru-cache/README.md) | Python OrderedDict and C++ list plus hash map maintain the same recency order; C++ stores stable list iterators. |
| [TimeMap](../problems/0981-time-based-key-value-store/README.md) | Per-key timestamp histories support binary search for the latest entry at or before a query. |
| [Mutable range sums](../problems/0307-range-sum-query-mutable/README.md) | Fenwick blocks receive a replacement's delta; C++ uses widened retained sums. |
| [Sliding Window Maximum](../problems/0239-sliding-window-maximum/README.md) | A deque stores candidate indexes, expires old positions, and discards values dominated by a newer one. |
| [Network Delay Time](../problems/0743-network-delay-time/README.md) | A min-heap carries distance candidates; obsolete distances are skipped. |
| [Connect All Points](../problems/1584-min-cost-to-connect-all-points/README.md) | Dense Prim keeps one best connection cost per remaining point without storing every edge. |

Each C++ design adapter creates a fresh local object for a legal history. Its JSON input is `[operations, arguments]`, and constructor/void operations produce `null`, matching Python's serialized `None`.

[Online Stock Span](../problems/0901-online-stock-span/README.md) accumulates spans when dominated prices leave its stack; count pushes and pops over the entire history for its amortized bound. [Circular Queue](../problems/0622-design-circular-queue/README.md) stores a logical size separately from its wrapped position, so a full queue and an empty queue cannot become ambiguous.

## Node ownership and local adapters

`solution.py` and `solution.cpp` retain LeetCode's class and method interfaces. The platform supplies node types; local adapters supply compatible definitions and construct nodes from JSON fixtures.

C++ [ListArena and TreeArena](../cpp/atlas_adapter.hpp) own nodes through `unique_ptr` storage. Submission methods receive borrowed raw pointers. Reverse Linked List rewires links; Remove Nth Node detaches a node without deleting it. Arena cleanup remains valid even when a node is no longer reachable from the returned head. Moving the owning pointers does not move the nodes themselves.

Trees use queue-based level-order encoding with `null` child positions. `[1,null,2,3]` means that 3 is the left child of 2, not an array-heap index. Serializers trim trailing nulls and reject cycles or shared-child structures. The C++ BST counterpart walks inorder with an explicit stack, taking O(n) time and O(h) auxiliary space.

[Construct Tree from Preorder/Inorder](../problems/0105-construct-binary-tree-from-preorder-and-inorder-traversal/README.md) allocates new nodes instead of borrowing an input arena. Its constructor stages ownership for exception safety, then the adapter's `TreeResultOwner` takes responsibility for the returned tree. Borrowed arena trees must not be transferred to this owner. Python's stack uses O(h) auxiliary space; the C++ ownership staging uses O(n), excluding the output in both bounds.

The Python adapter copies JSON inputs before constructing nodes or passing mutable values. For [Reorder List](../problems/0143-reorder-list/README.md) and [Move Zeroes](../problems/0283-move-zeroes/README.md), `result_from_arg: 0` selects the mutated first argument after the method returns `None`. Submission signatures remain unchanged.

[Add Two Numbers](../problems/0002-add-two-numbers/README.md) constructs a fresh result list; the adapter's `ListResultOwner` releases those nodes after serialization. [Merge K Sorted Lists](../problems/0023-merge-k-sorted-lists/README.md) receives several independently built lists and rewires borrowed nodes while the arena retains ownership. A new result and a rearrangement of existing nodes require different ownership paths.

Python LCA fixtures resolve query values to the original nodes in one adapted tree. The result serializer requires that the returned node belong to that tree; an equal value stored in a fresh node cannot substitute for identity. [Structural tests](verification.md) inspect links and references directly.

## Build and compare

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --parallel
ctest --test-dir build --output-on-failure
ATLAS_CPP_BIN_DIR=build/bin python -m pytest tests/test_cases.py tests/test_cpp_properties.py
```

The shared-fixture suite requires every configured counterpart runner. The generated suite includes 22,500 comparisons across 150 counterparts. New pairs declare valid input generation in their own `parity.py` module, while the earlier generators remain supported. Independent Python oracles provide another verification path because two language implementations can share the same algorithmic mistake.

See [verification](verification.md) for sanitizer settings, recorded command results, and the distinction between local checks and official judge evidence.

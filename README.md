# LeetCode Atlas

[![CI](https://github.com/michaelbawuah/LeetCode_Atlas/actions/workflows/ci.yml/badge.svg)](https://github.com/michaelbawuah/LeetCode_Atlas/actions/workflows/ci.yml)

An algorithm collection organized around **why a solution works**: the state it maintains, the invariant that makes it correct, and the counterexamples that test it.

<!-- atlas:stats:start -->
**150 distinct problems · 150 Python solutions · 75 C++23 counterparts**
<!-- atlas:stats:end -->

[Browse every problem](docs/problems.md) · [Explore patterns](docs/patterns.md) · [Follow algorithm traces](docs/traces.md) · [Run the checks](docs/verification.md) · [See the roadmap](docs/roadmap.md)

## Start with a pattern

Python is the primary interview-practice track; selected C++23 counterparts make container, arithmetic, ownership, and implementation tradeoffs visible. Every problem has submission-ready code, original reasoning, named fixtures, generated checks, and metadata. Both languages use the same fixtures, with 150 additional generated comparisons for every C++ counterpart.

| Family | Representative problem | What the explanation makes explicit |
|---|---|---|
| Hashing | [Longest Consecutive Sequence](problems/0128-longest-consecutive-sequence/README.md) | Start only at a sequence boundary. |
| Two pointers | [3Sum](problems/0015-3sum/README.md) | Which candidate pairs a pointer move eliminates. |
| Sliding window | [Minimum Window Substring](problems/0076-minimum-window-substring/README.md) | Track missing occurrences, including repeated letters. |
| Stack | [Daily Temperatures](problems/0739-daily-temperatures/README.md) | Each unresolved index is pushed and popped at most once. |
| Binary search | [Koko Eating Bananas](problems/0875-koko-eating-bananas/README.md) | Search a monotone feasibility boundary rather than an array index. |
| Linked lists | [Reorder List](problems/0143-reorder-list/README.md) | Split, reverse, and weave existing nodes without losing links. |
| Trees | [Validate Binary Search Tree](problems/0098-validate-binary-search-tree/README.md) | Strict global ordering, including ancestor constraints. |
| Intervals | [Merge Intervals](problems/0056-merge-intervals/README.md) | Maintain a completed prefix and one extendable range. |
| Heaps | [Find Median from Data Stream](problems/0295-find-median-from-data-stream/README.md) | Balance two partitions while preserving their value ordering. |
| Tries | [Implement Trie](problems/0208-implement-trie-prefix-tree/README.md) | A reachable prefix and a complete word are different states. |
| Backtracking | [Combination Sum](problems/0039-combination-sum/README.md) | Choose, explore, and undo with a rule that prevents duplicate combinations. |
| Graphs and dependencies | [Course Schedule II](problems/0210-course-schedule-ii/README.md) | Validate any complete ordering that respects every prerequisite. |
| Disjoint sets | [Redundant Connection](problems/0684-redundant-connection/README.md) | An edge inside one existing component closes a cycle. |
| Sequence and grid DP | [Longest Common Subsequence](problems/1143-longest-common-subsequence/README.md) · [Unique Paths](problems/0062-unique-paths/README.md) | Define the state before compressing its storage. |
| Shortest paths | [Network Delay Time](problems/0743-network-delay-time/README.md) | Separate the best known distance from an obsolete heap candidate. |
| Cache design | [LRU Cache](problems/0146-lru-cache/README.md) | Keep lookup and recency order synchronized. |
| Mutable range queries | [Range Sum Query — Mutable](problems/0307-range-sum-query-mutable/README.md) | Update only the prefix blocks affected by a changed value. |

The [full catalog](docs/problems.md) links every implementation, explanation, fixture, and property suite. The [generated pattern index](docs/pattern-index.md) lists every problem tagged with each technique.

## Run locally

Use Python 3.11 or newer, preferably inside a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest
python tools/catalog.py --check
```

For C++23, install CMake 3.24 or newer and a compatible compiler:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --parallel
ctest --test-dir build --output-on-failure
ATLAS_CPP_BIN_DIR=build/bin python -m pytest tests/test_cases.py tests/test_cpp_properties.py
```

See [verification](docs/verification.md) for the checks and [C++ notes](docs/cpp-notes.md) for language-specific differences and node ownership.

## Browse from the terminal

Filter by pattern, run a default fixture, or supply JSON arguments:

```bash
python -m atlas list --pattern trie
python -m atlas list --pattern dynamic-programming --difficulty Medium
python -m atlas run 1
python -m atlas run 1 --args '[[2,7,11,15],9]'
python -m atlas run 143
python -m atlas run 210
```

In-place methods keep their LeetCode interface: Reorder List and Move Zeroes return `None`, while local metadata tells the adapter which mutated argument to display. Design problems use their named operation-sequence fixtures.

## Read a solution

Start with the baseline, identify the repeated work, and state the optimized algorithm's invariant before reading its code. Each explanation includes complexity, pitfalls, and a follow-up that changes one assumption. Tests compare independently expressed answers or inspect structural behavior such as node reuse and absence of cycles.

Official LeetCode submission evidence is tracked separately from local verification. Current entries have no recorded official acceptances.

## Grow the atlas

The **25 / 10 foundation**, **75 / 25 essential-pattern milestone**, and **150 / 75 interview core** are present. The next cumulative target is **300 Python / 150 C++23**. The [roadmap](docs/roadmap.md) describes the remaining coverage and practice goals.

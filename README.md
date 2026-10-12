# LeetCode Atlas

[![CI](https://github.com/michaelbawuah/LeetCode_Atlas/actions/workflows/ci.yml/badge.svg)](https://github.com/michaelbawuah/LeetCode_Atlas/actions/workflows/ci.yml)

An algorithm collection organized around **why a solution works**: the state it maintains, the invariant that makes it correct, and the counterexamples that test it.

**25 distinct problems · 25 Python solutions · 10 C++23 counterparts**

[Browse every problem](docs/problems.md) · [Explore patterns](docs/patterns.md) · [Run the checks](docs/verification.md) · [See the roadmap](docs/roadmap.md)

## Start with a pattern

Every problem folder contains submission-ready code, an explanation, named test cases, generated-input checks, and structured metadata. The foundation includes 180 named fixtures and 1,500 generated Python/C++ comparison cases. The C++ track uses the same fixtures as Python.

| Pattern and representative problem | Source | Explanation | Fixtures | Generated checks |
|---|---|---|---|---|
| Hash lookup: [Two Sum](problems/0001-two-sum/) | [Python](problems/0001-two-sum/solution.py) · [C++](problems/0001-two-sum/solution.cpp) | [Notes](problems/0001-two-sum/README.md) | [Cases](problems/0001-two-sum/cases.json) | [Properties](problems/0001-two-sum/test_properties.py) |
| Two pointers: [3Sum](problems/0015-3sum/) | [Python](problems/0015-3sum/solution.py) · [C++](problems/0015-3sum/solution.cpp) | [Notes](problems/0015-3sum/README.md) | [Cases](problems/0015-3sum/cases.json) | [Properties](problems/0015-3sum/test_properties.py) |
| Sliding window: [Longest Substring](problems/0003-longest-substring-without-repeating-characters/) | [Python](problems/0003-longest-substring-without-repeating-characters/solution.py) · [C++](problems/0003-longest-substring-without-repeating-characters/solution.cpp) | [Notes](problems/0003-longest-substring-without-repeating-characters/README.md) | [Cases](problems/0003-longest-substring-without-repeating-characters/cases.json) | [Properties](problems/0003-longest-substring-without-repeating-characters/test_properties.py) |
| Prefix/suffix state: [Product Except Self](problems/0238-product-of-array-except-self/) | [Python](problems/0238-product-of-array-except-self/solution.py) · [C++](problems/0238-product-of-array-except-self/solution.cpp) | [Notes](problems/0238-product-of-array-except-self/README.md) | [Cases](problems/0238-product-of-array-except-self/cases.json) | [Properties](problems/0238-product-of-array-except-self/test_properties.py) |
| Stack: [Valid Parentheses](problems/0020-valid-parentheses/) | [Python](problems/0020-valid-parentheses/solution.py) · [C++](problems/0020-valid-parentheses/solution.cpp) | [Notes](problems/0020-valid-parentheses/README.md) | [Cases](problems/0020-valid-parentheses/cases.json) | [Properties](problems/0020-valid-parentheses/test_properties.py) |
| Monotonic stack: [Daily Temperatures](problems/0739-daily-temperatures/) | [Python](problems/0739-daily-temperatures/solution.py) · [C++](problems/0739-daily-temperatures/solution.cpp) | [Notes](problems/0739-daily-temperatures/README.md) | [Cases](problems/0739-daily-temperatures/cases.json) | [Properties](problems/0739-daily-temperatures/test_properties.py) |
| Binary search: [Rotated Array Search](problems/0033-search-in-rotated-sorted-array/) | [Python](problems/0033-search-in-rotated-sorted-array/solution.py) · [C++](problems/0033-search-in-rotated-sorted-array/solution.cpp) | [Notes](problems/0033-search-in-rotated-sorted-array/README.md) | [Cases](problems/0033-search-in-rotated-sorted-array/cases.json) | [Properties](problems/0033-search-in-rotated-sorted-array/test_properties.py) |
| Linked-list pointers: [Reverse Linked List](problems/0206-reverse-linked-list/) | [Python](problems/0206-reverse-linked-list/solution.py) · [C++](problems/0206-reverse-linked-list/solution.cpp) | [Notes](problems/0206-reverse-linked-list/README.md) | [Cases](problems/0206-reverse-linked-list/cases.json) | [Properties](problems/0206-reverse-linked-list/test_properties.py) |
| Tree traversal: [Level Order Traversal](problems/0102-binary-tree-level-order-traversal/) | [Python](problems/0102-binary-tree-level-order-traversal/solution.py) | [Notes](problems/0102-binary-tree-level-order-traversal/README.md) | [Cases](problems/0102-binary-tree-level-order-traversal/cases.json) | [Properties](problems/0102-binary-tree-level-order-traversal/test_properties.py) |
| Graph traversal: [Number of Islands](problems/0200-number-of-islands/) | [Python](problems/0200-number-of-islands/solution.py) | [Notes](problems/0200-number-of-islands/README.md) | [Cases](problems/0200-number-of-islands/cases.json) | [Properties](problems/0200-number-of-islands/test_properties.py) |
| Dynamic programming: [House Robber](problems/0198-house-robber/) | [Python](problems/0198-house-robber/solution.py) · [C++](problems/0198-house-robber/solution.cpp) | [Notes](problems/0198-house-robber/README.md) | [Cases](problems/0198-house-robber/cases.json) | [Properties](problems/0198-house-robber/test_properties.py) |

The [full catalog](docs/problems.md) includes difficulty, patterns, available languages, and links to all 25 entries.

## Run locally

Use Python 3.11 or newer, preferably inside a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest
python tools/catalog.py --check
```

For the C++23 track, install CMake 3.24 or newer and a C++23-capable compiler, then build and include the runners in the shared-case tests:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --parallel
ctest --test-dir build --output-on-failure
ATLAS_CPP_BIN_DIR=build/bin python -m pytest tests/test_cases.py
```

See [verification](docs/verification.md) for the different checks and [C++ notes](docs/cpp-notes.md) for language-specific implementation details.

## Browse from the terminal

Filter the catalog by pattern, run a problem's default fixture, or supply one input directly:

```bash
python -m atlas list --pattern binary-search
python -m atlas run 1
python -m atlas run 1 --args '[[2,7,11,15],9]'
```

## Read a solution

Start with the baseline, identify what repeated work can be removed, and state the optimized algorithm's invariant before reading the code. Each explanation includes complexity, edge cases, and a follow-up that changes one assumption.

Local fixtures and generated tests have their own verification path. Official LeetCode submission results are tracked separately in metadata; none are recorded yet.

## Grow the atlas

The next cumulative milestones are **75 / 25**, **150 / 75**, and **300 / 150** Python problems / C++ counterparts. Additions should expand pattern coverage and bring explanations and tests with the code. The [roadmap](docs/roadmap.md) describes the sequence.

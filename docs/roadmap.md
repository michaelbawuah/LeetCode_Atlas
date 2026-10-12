# Roadmap

[Problem catalog](problems.md) · [Pattern atlas](patterns.md) · [Repository](../README.md)

Python is the primary track for software engineering and AI/ML interview practice. Selected C++23 counterparts build fluency for quant engineering and make language-specific differences visible.

## Cumulative milestones

| Milestone | Distinct Python problems | C++23 counterparts | Focus |
|---|---:|---:|---|
| Foundation | **25** | **10** | Repository structure, core patterns, independent tests, shared fixtures |
| Essential patterns | 75 | 25 | Broader coverage and variations of familiar techniques |
| Interview core | 150 | 75 | Mixed-pattern problems, harder transitions, systematic re-solving |
| Main target | **300** | **150** | Complete explanations across the major interview families |

These are cumulative counts. At the main target, 300 distinct problems would have 450 language implementations. The foundation's 25 Python entries and 10 C++ counterparts are present in the repository; later rows are targets.

## After the foundation

**To 75:** add intervals, linked-list cycle techniques, heaps, tree search, backtracking, and basic multidimensional dynamic programming. Expand binary search from index lookup to monotone feasibility predicates. Include bit-manipulation problems with clear integer assumptions.

**To 150:** add union-find, topological ordering, shortest paths, tries, sequence dynamic programming, and problems that combine several patterns. Choose C++ counterparts where ownership, containers, numeric limits, or state representation offer a useful comparison.

**To 300:** add harder graph and dynamic programming variations, systematic boundary cases, and multiple approaches where their tradeoffs are substantial. A planned difficulty mix is 60 Easy, 195 Medium, and 45 Hard; coverage and explanation quality guide the actual selection.

## What belongs with each addition

| File | Purpose |
|---|---|
| `solution.py` | Submission-ready Python implementation |
| `README.md` | Intuition, baseline, optimized approach, correctness, complexity, pitfalls, follow-up |
| `cases.json` | Named examples and meaningful boundaries |
| `test_properties.py` | Independent oracle or structural checks on generated inputs |
| `meta.json` | Problem identity, method signature, patterns, checker, complexity, judge status |
| `solution.cpp` and `cpp_runner.cpp`, when selected | C++23 implementation and local adapter using the shared fixtures |

Tests should challenge a failure mode or compare against an independently expressed result. A generated test that simply repeats the optimized implementation adds little confidence.

## Practice alongside the collection

Use a separate practice record for timed attempts, explanations, and re-solves. The repository catalog counts implementations; it does not infer those activities from the presence of a file. After revisiting a problem, try its follow-up or solve it without looking at the implementation.

Meaningful commits can group a solution with its explanation and tests, or capture a substantive improvement. Keep the generated catalog synchronized as problems and language counterparts are added.

## Later extensions

A SQL track can add database interview problems and reproducible fixtures. A searchable companion guide can be built from the same metadata once the catalog grows. Neither extension is part of the current foundation.

500 distinct problems is a possible stretch target after the 300-problem core, guided by remaining gaps rather than a predetermined volume of additions.

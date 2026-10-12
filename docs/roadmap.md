# Roadmap

[Problem catalog](problems.md) · [Pattern atlas](patterns.md) · [Repository](../README.md)

Python is the primary track for software engineering and AI/ML interview practice. Selected C++23 counterparts build fluency for quant engineering and make language-specific differences visible.

## Cumulative milestones

| Milestone | Distinct Python problems | C++23 counterparts | Status | Focus |
|---|---:|---:|---|---|
| Foundation | 25 | 10 | Present | Core patterns, repository structure, independent tests, shared fixtures |
| Essential patterns | **75** | **25** | Present | Intervals, heaps, tries, backtracking, graph components and dependencies, sequence/grid DP |
| Interview core | 150 | 75 | Next target | Mixed-pattern problems, deeper graph algorithms, harder transitions, systematic re-solving |
| Main target | **300** | **150** | Target | Broad explanations across the major interview families |

Counts are cumulative: the current milestone contains 100 language implementations covering 75 distinct problems. The main target would contain 450 implementations covering 300 problems. See [verification records](verification.md) for evidence associated with each milestone.

## Next: 150 Python / 75 C++23

Build on the existing graph, trie, and DP foundations with shortest paths, weighted graphs, advanced tree queries, string algorithms, and mixed-pattern problems. Expand DP to interval states and less direct transitions. Add C++ counterparts where ownership, numeric bounds, container behavior, or a different algorithm provides a useful comparison.

Practice should accompany expansion: revisit the essential patterns under time limits, explain their invariants aloud, and record which follow-ups still expose gaps. A familiar implementation alone does not demonstrate independent recall.

## Then: 300 Python / 150 C++23

Add harder graph and DP variations, substantial alternative approaches, and systematic boundary cases. A planned difficulty mix is 60 Easy, 195 Medium, and 45 Hard; coverage and explanation quality guide the actual selection.

The existing interval, heap, trie, topological-order, union-find, and sequence/grid DP entries provide starting points for these deeper variations. The [pattern atlas](patterns.md) connects representative implementations to the state they retain.

## What belongs with each addition

| File | Purpose |
|---|---|
| `solution.py` | Submission-ready Python implementation |
| `README.md` | Intuition, baseline, approach, correctness, complexity, pitfalls, follow-up |
| `cases.json` | Named examples and meaningful boundaries |
| `test_properties.py` | Independent oracle or structural checks on generated inputs |
| `meta.json` | Identity, interface, patterns, checker, complexity, judge status; in-place result argument where needed |
| `solution.cpp` and `cpp_runner.cpp`, when selected | C++23 implementation and adapter using shared fixtures |

Tests should challenge a failure mode or compare against an independently expressed result. A generated test that repeats the optimized implementation adds little confidence. Stateful interfaces need legal operation histories, and outputs with several valid witnesses need semantic checks.

## Practice alongside the collection

Use a separate record for timed attempts, explanations, and re-solves. The catalog counts implementations; it does not infer those activities from a file. After revisiting a problem, try its follow-up or solve it without looking at the implementation.

Meaningful commits can group a solution with its reasoning and tests, or capture a substantive improvement. Keep generated navigation synchronized as problems and counterparts are added.

## Later extensions

A SQL track can add database interview problems and reproducible fixtures. A searchable companion guide can use the same metadata. Both remain optional extensions beyond the current 75-problem collection.

500 distinct problems is a possible stretch target after the 300-problem core, guided by remaining gaps rather than a predetermined volume of additions.

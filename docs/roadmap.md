# Roadmap

[Problem catalog](problems.md) · [Pattern atlas](patterns.md) · [Repository](../README.md)

Python is the primary track for software engineering and AI/ML interview practice. Selected C++23 counterparts build fluency for quant engineering and make language-specific differences visible.

## Cumulative milestones

| Milestone | Distinct Python problems | C++23 counterparts | Status | Focus |
|---|---:|---:|---|---|
| Foundation | 25 | 10 | Present | Core patterns, repository structure, independent tests, shared fixtures |
| Essential patterns | **75** | **25** | Present | Intervals, heaps, tries, backtracking, graph components and dependencies, sequence/grid DP |
| Interview core | **150** | **75** | Present | Weighted graphs, tree reconstruction, string/counting DP, duplicate-aware search, stateful designs |
| Main target | **300** | **150** | Present | Interval DP, string matching, bridges, tree relationships, extended stateful designs |

Counts are cumulative: the current milestone contains 450 language implementations covering 300 distinct problems. This is a custom interview collection, not a claim to reproduce a particular official study plan. See [verification records](verification.md) for evidence associated with each milestone.

## Present: 150 Python / 75 C++23

The expanded collection covers Dijkstra, bounded-edge relaxation, minimum spanning trees, graph cloning, tree reconstruction, linked-list groups and cycles, string/counting DP, and duplicate-aware backtracking. Stateful additions include LRU Cache, TimeMap, Twitter, snapshots, and mutable range queries. The [worked traces](traces.md) illustrate representative state transitions.

Practice should accompany expansion: revisit the essential patterns under time limits, explain their invariants aloud, and record which follow-ups still expose gaps. A familiar implementation alone does not demonstrate independent recall.

## Present: 300 Python / 150 C++23

The main target adds interval DP, KMP prefix reuse, graph bridges and safe states, constrained paths, tree relationships, and legal operation histories for calendars and circular buffers. Selected C++ counterparts expose fresh-node ownership, integer bounds, character handling, and container behavior. The [practice routes](practice.md) connect these topics to repeatable attempts and explanations.

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

A SQL track can add database interview problems and reproducible fixtures. A searchable companion guide can use the same metadata. Both remain optional extensions beyond the current 300-problem collection.

500 distinct problems is a possible stretch target after the 300-problem core, guided by remaining gaps rather than a predetermined volume of additions.

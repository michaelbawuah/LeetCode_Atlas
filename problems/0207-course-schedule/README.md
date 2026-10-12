# 207 · Course Schedule

[Problem](https://leetcode.com/problems/course-schedule/) · Medium

## Idea

A course becomes available only after all incoming prerequisite edges have been removed. Start with courses having no prerequisites, then release their dependents as courses are completed.

**Baseline:** enumerate every course ordering and test every prerequisite, costing O(V! · (V + E)). The chosen approach uses an indegree array and a queue.

## Why it works

The queue contains exactly the unprocessed courses with no unfinished prerequisite. Taking one is always legal, and removing its outgoing edges updates that invariant. If the queue empties early, every remaining vertex has an incoming edge from the remaining graph; following such edges eventually repeats a vertex, proving a cycle. Thus all courses finish exactly when the graph is acyclic.

## Complexity

For V courses and E prerequisite pairs, O(V + E) time and O(V + E) space for adjacency lists, indegrees, and the queue. Inputs are not modified.

## Counterexample and checks

Checking whether at least one course is initially ready is insufficient: an independent course can coexist with a cycle elsewhere. Named cases include disconnected cycles; generated tests compare against exhaustive permutations of small graphs.

**Follow-up:** return a concrete cycle as an explanation when completion is impossible.

## Python and C++23 comparison

Both implementations use Kahn's algorithm with adjacency lists, indegrees, and a ready queue. Python uses `deque`; C++ uses `std::queue<int>` and vectors. Each vertex is queued once and each edge is removed once, giving O(V + E) time and O(V + E) auxiliary storage. The returned boolean needs constant space, and neither implementation modifies the prerequisite list.

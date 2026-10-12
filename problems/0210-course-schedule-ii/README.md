# 210 · Course Schedule II

[Problem](https://leetcode.com/problems/course-schedule-ii/) · Medium

## Idea

Build a course ordering as courses become ready. Indegrees record unfinished prerequisites; a queue starts with courses having none. Processing a course can make its dependents ready.

**Baseline:** enumerate permutations and check each prerequisite. The chosen O(V + E) algorithm constructs an ordering directly rather than searching every possible ordering.

## Why it works

Every emitted course has no prerequisite remaining in the unprocessed graph. Its prerequisites therefore appear earlier in the result. If V courses are emitted, the result satisfies every directed edge and includes every course once. If fewer are emitted, the remaining graph contains a directed cycle, and no complete ordering exists.

## Complexity

O(V + E) time and O(V + E) total space, including the O(V) output. The input edges are not modified.

## Counterexample and checks

Sorting course IDs ignores dependencies: an edge requiring course 3 before course 0 invalidates numerical order. More than one ordering can be correct; fixtures use a semantic checker that verifies vertex coverage and prerequisite order instead of matching one arbitrary list. Generated tests establish existence independently by enumerating small permutations.

**Follow-up:** use a min-heap to return the lexicographically smallest valid ordering, and account for its additional cost.

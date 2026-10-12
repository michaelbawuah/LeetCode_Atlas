# 621 · Task Scheduler

[Problem](https://leetcode.com/problems/task-scheduler/) · Medium

## Idea

Let f be the largest task frequency and t the number of task types tied at f. The f−1 gaps between repeated most-common tasks impose a frame of `(f−1)(cooldown+1)+t` slots. Enough other tasks can fill that frame; otherwise idles remain necessary.

**Baseline:** enumerate task and idle choices while tracking per-type cooldowns. Frequency structure avoids searching schedules.

## Why it works

Every schedule needs at least N slots for N tasks. Separating f copies of each most-frequent type also needs at least f−1 groups of cooldown+1 slots and t trailing maximum-frequency tasks. Less-frequent tasks can be distributed among those gaps; if they overflow the frame, their extra slots supply the necessary separation. Thus the larger of N and the frame lower bound is attainable and optimal.

## Complexity

O(N) time to count tasks and O(1) auxiliary space under the fixed 26-uppercase-letter alphabet, with scalar output. The task list is unchanged.

## Counterexample and checks

Counting only one most-frequent task misses ties: three types each appearing twice with cooldown 2 fit six slots. The independent oracle explores legal task executions and idle choices with exact remaining counts and cooldown states on small inputs.

**Follow-up:** construct an actual optimal schedule and explain how its output size affects space complexity.

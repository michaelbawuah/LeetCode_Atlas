# 225. Implement Stack using Queues

[Problem on LeetCode](https://leetcode.com/problems/implement-stack-using-queues/) · Easy

## Approach, invariant, and complexity

Use one queue and rotate its previous contents behind every new value. Its front then always represents the stack top.

A baseline with two queues moves elements during pop; this variant pays the movement cost during push. After each operation the queue contains values in reverse insertion order. Appending a new value and moving all older queue entries behind it preserves that order, so front access and removal implement last-in, first-out behavior.

push takes O(n) time for n existing values; pop, top, and empty take O(1). Stored space is O(n). Only queue-front access, front removal, back insertion, and size/emptiness are used.

pop and top are only called on nonempty state. Repeated values remain separate stack entries.

Follow-up: move the O(n) work to pop instead. Compare the costs for workloads dominated by pushes.

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

## C++23 counterpart

C++ uses std::queue and only its front, push, pop, size, and empty operations. Each push rotates the previous n entries behind the new front. pop and top require nonempty state; generated histories enforce that precondition.

Time: push O(n); pop/top/empty O(1). Space: O(n).

The JSON adapter creates fresh state per case. Named fixtures and 150 deterministic generated inputs compare the two language implementations; existing independent Python oracles supply a separate behavioral reference.

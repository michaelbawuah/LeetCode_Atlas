# 232. Implement Queue using Stacks

[Problem on LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/) · Easy

## Approach, invariant, and complexity

Incoming values stack in arrival order; transferring them to a second stack reverses that order so its top is the oldest value.

A baseline reverses the stack for every read, O(n) per query. Here a transfer occurs only when the outgoing stack is empty. The logical queue is outgoing values read top-to-bottom followed by incoming values read bottom-to-top. That invariant makes outgoing top the correct next value. New pushes stay behind any existing outgoing values.

push, pop, and peek take O(1) amortized time across a sequence; a single transfer can take O(n). Each element crosses stacks at most once before removal. empty takes O(1), and stored space is O(n).

Do not transfer into a nonempty outgoing stack, which would move newer values ahead of older ones. pop and peek have a nonempty precondition.

Follow-up: support a minimum query by storing prefix minima in both stacks.

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.

## C++23 counterpart

C++ uses two std::stack instances backed by their default deques. Transfer only when outgoing is empty, so each value crosses once before removal. A read may transfer n values, while the total cost over a valid history is linear in the number of operations.

Time: push O(1); pop/peek O(1) amortized, O(n) worst-case; empty O(1). Space: O(n).

The JSON adapter creates fresh state per case. Named fixtures and 150 deterministic generated inputs compare the two language implementations; existing independent Python oracles supply a separate behavioral reference.

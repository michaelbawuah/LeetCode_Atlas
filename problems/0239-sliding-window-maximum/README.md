# 239 · Sliding Window Maximum

[Problem](https://leetcode.com/problems/sliding-window-maximum/) · Hard · Monotonic deque

## Approach

**Baseline:** scan every window for its maximum: O(nk) time.
**Chosen approach:** keep candidate indices in a deque, with their values strictly
decreasing. Expire old indices at the front and remove dominated candidates at the back.

## Invariant and correctness

Deque indices increase and all belong to the active window. If a new value is
at least an older candidate's value, the older index can never win a future
window: the new value is no smaller and expires later. Discarding it is safe.
After expiration and dominance removal, the front has the largest remaining
value and therefore gives the current window maximum. Keeping newer equal values
also maintains the same guarantee.

## Complexity and languages

Both implementations use O(n) time because each index is inserted and removed
at most once. Auxiliary space is O(k), plus O(n - k + 1) output. Both preserve input.
C++ passes the vector by reference, reserves output capacity, and guards subtraction
before comparing unsigned indices with an expiration boundary.

## Verification and pitfalls

Properties independently call `max` on every window and check reversal. Test
unit/full windows, ties, negative values, and monotone sequences. Store indices,
not only values, to distinguish expiration from equal-valued replacements.

**Follow-up:** how would two-stack window aggregation handle a different associative operation?

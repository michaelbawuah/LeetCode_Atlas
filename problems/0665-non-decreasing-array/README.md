# 665 · Non-decreasing Array

[Problem](https://leetcode.com/problems/non-decreasing-array/) · Medium

## Idea and approaches

Repair a first decrease virtually, choosing whether to lower the previous value or raise the current value. Trying every position and replacement is the baseline; the scan needs one change counter.

## Correctness invariant

Before a decrease, the prefix is already nondecreasing. Lowering its last value to the current value is safe if it does not fall below the preceding prefix value, and gives the smallest possible current bound. Otherwise that previous value must remain and the current value is virtually raised to it. These are the only useful one-position repairs. A second decrease against the resulting virtual previous value proves no remaining change is available.

## Complexity

O(n) time and O(1) auxiliary space. The virtual repair preserves the caller array instead of making a copy or changing its values.

## Verification and pitfalls

The independent oracle enumerates every one-position replacement on small arrays. Cases distinguish lowering the first entry, raising an interior entry, and the unrecoverable 3,4,2,3 pattern.

Checking only that there is one original adjacent decrease is insufficient; its neighbors determine whether either repair is viable.

**Follow-up:** What extra state would be necessary if two replacements were permitted?

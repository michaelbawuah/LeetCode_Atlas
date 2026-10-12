# 76 · Minimum Window Substring

[Problem](https://leetcode.com/problems/minimum-window-substring/) · Hard · Sliding window

## Idea

Track the remaining required occurrences, including repeated letters. Expand the
right edge until the window covers the target, then shrink its left edge while
coverage remains valid.

**Baseline:** enumerate substrings and count each one's letters, taking O(n³)
time in a direct implementation.
**Chosen approach:** maintain a counter of target counts minus current window
counts. Positive values mean missing occurrences; zero or negative values mean
enough copies. A separate `missing` count makes validity checks constant-time.

## Why it works

After each edge update, the counter represents the occurrence deficit and
`missing` counts its positive deficits. Thus zero means the window covers the
target. For every right endpoint, shrinking records all valid left endpoints
until removing one required occurrence breaks coverage. The smallest recorded
window is globally minimal; no earlier discarded left endpoint could later
produce a smaller answer than the valid window already recorded before discarding it.

## Complexity

Python: O(|s| + |t|) expected time and O(σ) auxiliary space, where σ counts
distinct encountered characters, plus O(w) for the returned window of length w.
Both pointers move forward at most |s| times. The allowed English alphabet bounds σ.

## Tests and pitfalls

Cover repeated requirements, missing letters, case differences, and suffix minima.
The exhaustive oracle checks all short substrings. It checks optimal length and
coverage even on generated ties; official fixtures have unique shortest answers.
Tracking only distinct letters fails when the target needs multiple copies.

**Follow-up:** what changes if matching ignores case or includes normalized Unicode?

## Python and C++23 comparison

Python uses a `Counter` keyed by characters. C++ uses a fixed 256-entry deficit array indexed through `unsigned char`, suitable for the problem's English-letter byte alphabet and avoiding negative indexes from signed `char`. Both move each window boundary forward at most |s| times; C++ takes O(|s| + |t|) time with O(1) counter and index state. Its `string s, string t` parameters are passed by value, so ordinary calls with existing input strings also copy O(|s| + |t|) characters. Returning the winning substring allocates O(w) characters for window length w. Counting those parameter copies is distinct from the constant working state. Neither implementation changes the caller's strings.

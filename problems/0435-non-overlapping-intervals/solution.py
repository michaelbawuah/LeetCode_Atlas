class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        ordered = sorted(intervals, key=lambda interval: interval[1])
        kept = 0
        previous_end: int | None = None
        for start, end in ordered:
            if previous_end is None or start >= previous_end:
                kept += 1
                previous_end = end
        return len(intervals) - kept

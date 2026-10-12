from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waits = [0] * len(temperatures)
        pending = []
        for day, temperature in enumerate(temperatures):
            while pending and temperatures[pending[-1]] < temperature:
                previous_day = pending.pop()
                waits[previous_day] = day - previous_day
            pending.append(day)
        return waits

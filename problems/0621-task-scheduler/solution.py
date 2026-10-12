from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        largest = max(counts.values())
        ties = sum(frequency == largest for frequency in counts.values())
        frame = (largest - 1) * (n + 1) + ties
        return max(len(tasks), frame)

from collections import deque


class RecentCounter:
    def __init__(self):
        self._times = deque()

    def ping(self, t: int) -> int:
        self._times.append(t)
        while self._times[0] < t - 3000:
            self._times.popleft()
        return len(self._times)

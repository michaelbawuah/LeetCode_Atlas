from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self._history = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._history.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        history = self._history.get(key, [])
        index = bisect_right(history, timestamp, key=lambda entry: entry[0]) - 1
        return history[index][1] if index >= 0 else ""

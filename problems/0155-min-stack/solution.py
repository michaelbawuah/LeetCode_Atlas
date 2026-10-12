class MinStack:
    def __init__(self):
        self._entries = []

    def push(self, val: int) -> None:
        minimum = min(val, self._entries[-1][1]) if self._entries else val
        self._entries.append((val, minimum))

    def pop(self) -> None:
        self._entries.pop()

    def top(self) -> int:
        return self._entries[-1][0]

    def getMin(self) -> int:
        return self._entries[-1][1]

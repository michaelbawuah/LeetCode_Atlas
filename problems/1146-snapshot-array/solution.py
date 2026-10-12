from bisect import bisect_right


class SnapshotArray:
    def __init__(self, length: int):
        self._id = 0
        self._history = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        history = self._history[index]
        if history[-1][0] == self._id:
            history[-1] = (self._id, val)
        else:
            history.append((self._id, val))

    def snap(self) -> int:
        result = self._id
        self._id += 1
        return result

    def get(self, index: int, snap_id: int) -> int:
        history = self._history[index]
        position = bisect_right(history, snap_id, key=lambda entry: entry[0]) - 1
        return history[position][1]

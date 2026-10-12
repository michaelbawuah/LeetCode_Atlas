class MyHashSet:
    def __init__(self):
        self._present = [False] * 1000001

    def add(self, key: int) -> None:
        self._present[key] = True

    def remove(self, key: int) -> None:
        self._present[key] = False

    def contains(self, key: int) -> bool:
        return self._present[key]

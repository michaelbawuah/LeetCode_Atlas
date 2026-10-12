class MyHashMap:
    def __init__(self):
        self._values = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self._values[key] = value

    def get(self, key: int) -> int:
        return self._values[key]

    def remove(self, key: int) -> None:
        self._values[key] = -1

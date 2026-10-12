class MyCircularQueue:
    def __init__(self, k: int):
        self._data = [0] * k
        self._head = 0
        self._size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._data[(self._head + self._size) % len(self._data)] = value
        self._size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._head = (self._head + 1) % len(self._data)
        self._size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self._data[self._head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self._data[(self._head + self._size - 1) % len(self._data)]

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == len(self._data)

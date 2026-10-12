from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self._values = list(nums)
        self._tree = [0] + list(nums)
        for index in range(1, len(self._tree)):
            parent = index + (index & -index)
            if parent < len(self._tree):
                self._tree[parent] += self._tree[index]

    def update(self, index: int, val: int) -> None:
        change = val - self._values[index]
        self._values[index] = val
        index += 1
        while index < len(self._tree):
            self._tree[index] += change
            index += index & -index

    def _prefix(self, end: int) -> int:
        total = 0
        while end:
            total += self._tree[end]
            end -= end & -end
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix(right + 1) - self._prefix(left)

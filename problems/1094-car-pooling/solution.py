class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        changes: dict[int, int] = {}
        for passengers, start, end in trips:
            changes[start] = changes.get(start, 0) + passengers
            changes[end] = changes.get(end, 0) - passengers
        load = 0
        for location in sorted(changes):
            load += changes[location]
            if load > capacity:
                return False
        return True

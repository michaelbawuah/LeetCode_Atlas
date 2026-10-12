class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        seen, pending = {0}, [0]
        while pending:
            for neighbor in rooms[pending.pop()]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
        return len(seen) == len(rooms)

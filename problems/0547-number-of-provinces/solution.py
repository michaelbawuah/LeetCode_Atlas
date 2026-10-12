class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        count = len(isConnected)
        seen = [False] * count
        provinces = 0
        for start in range(count):
            if seen[start]:
                continue
            provinces += 1
            seen[start] = True
            pending = [start]
            while pending:
                city = pending.pop()
                for neighbor, connected in enumerate(isConnected[city]):
                    if connected and not seen[neighbor]:
                        seen[neighbor] = True
                        pending.append(neighbor)
        return provinces

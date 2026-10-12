class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        adjacent = [[] for _ in range(n)]
        for index, (a, b) in enumerate(connections):
            adjacent[a].append((b, index))
            adjacent[b].append((a, index))
        discovery = [-1] * n
        low = [0] * n
        timer = 0
        bridges = []
        for start in range(n):
            if discovery[start] != -1:
                continue
            discovery[start] = low[start] = timer
            timer += 1
            stack = [[start, -1, 0]]
            while stack:
                node, parent_edge, offset = stack[-1]
                if offset < len(adjacent[node]):
                    neighbor, edge = adjacent[node][offset]
                    stack[-1][2] += 1
                    if edge == parent_edge:
                        continue
                    if discovery[neighbor] == -1:
                        discovery[neighbor] = low[neighbor] = timer
                        timer += 1
                        stack.append([neighbor, edge, 0])
                    else:
                        low[node] = min(low[node], discovery[neighbor])
                else:
                    stack.pop()
                    if parent_edge != -1:
                        a, b = connections[parent_edge]
                        parent = b if a == node else a
                        if low[node] > discovery[parent]:
                            bridges.append([parent, node])
                        low[parent] = min(low[parent], low[node])
        return bridges

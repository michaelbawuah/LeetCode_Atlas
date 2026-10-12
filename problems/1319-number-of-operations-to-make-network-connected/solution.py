class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        parent = list(range(n))
        size = [1] * n
        components = n

        def root(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for a, b in connections:
            a, b = root(a), root(b)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
                components -= 1
        return components - 1

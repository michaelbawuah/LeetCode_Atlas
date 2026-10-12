class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        sizes = [1] * n

        def root(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for a, b in edges:
            a, b = root(a), root(b)
            if a != b:
                if sizes[a] < sizes[b]:
                    a, b = b, a
                parent[b] = a
                sizes[a] += sizes[b]
        return root(source) == root(destination)

class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))
        sizes = [1] * len(parent)
        regions = len(parent)

        def root(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def join(a, b):
            nonlocal regions
            a, b = root(a), root(b)
            if a != b:
                if sizes[a] < sizes[b]:
                    a, b = b, a
                parent[b] = a
                sizes[a] += sizes[b]
                regions -= 1

        for row in range(n):
            for col in range(n):
                base = 4 * (row * n + col)
                if grid[row][col] != "/":
                    join(base, base + 1)
                    join(base + 2, base + 3)
                if grid[row][col] != chr(92):
                    join(base, base + 3)
                    join(base + 1, base + 2)
                if row + 1 < n:
                    join(base + 2, base + 4 * n)
                if col + 1 < n:
                    join(base + 1, base + 7)
        return regions

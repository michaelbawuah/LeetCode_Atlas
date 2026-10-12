class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        identity = {}
        parent = []
        size = []

        def index(key):
            if key not in identity:
                identity[key] = len(parent)
                parent.append(len(parent))
                size.append(1)
            return identity[key]

        def root(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for row, col in stones:
            first, last = root(index(("r", row))), root(index(("c", col)))
            if first != last:
                if size[first] < size[last]:
                    first, last = last, first
                parent[last] = first
                size[first] += size[last]
        components = {root(index(("r", row))) for row, _ in stones}
        return len(stones) - len(components)

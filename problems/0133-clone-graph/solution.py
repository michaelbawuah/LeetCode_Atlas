from collections import deque


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if node is None:
            return None
        copies = {node: Node(node.val)}
        pending = deque([node])
        while pending:
            current = pending.popleft()
            for neighbor in current.neighbors:
                if neighbor not in copies:
                    copies[neighbor] = Node(neighbor.val)
                    pending.append(neighbor)
                copies[current].neighbors.append(copies[neighbor])
        return copies[node]

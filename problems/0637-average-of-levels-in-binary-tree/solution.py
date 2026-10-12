from collections import deque
from typing import List, Optional


class Solution:
    def averageOfLevels(self, root: "Optional[TreeNode]") -> List[float]:
        pending = deque([root])
        averages = []
        while pending:
            count = len(pending)
            total = 0
            for _ in range(count):
                node = pending.popleft()
                total += node.val
                if node.left is not None:
                    pending.append(node.left)
                if node.right is not None:
                    pending.append(node.right)
            averages.append(total / count)
        return averages

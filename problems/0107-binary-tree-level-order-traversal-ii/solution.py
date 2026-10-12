from collections import deque
from typing import List, Optional


class Solution:
    def levelOrderBottom(self, root: "Optional[TreeNode]") -> List[List[int]]:
        pending = deque([root]) if root is not None else deque()
        result = []
        while pending:
            row = []
            for _ in range(len(pending)):
                node = pending.popleft()
                row.append(node.val)
                if node.left is not None:
                    pending.append(node.left)
                if node.right is not None:
                    pending.append(node.right)
            result.append(row)
        result.reverse()
        return result

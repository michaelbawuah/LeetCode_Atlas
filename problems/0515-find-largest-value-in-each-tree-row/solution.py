from collections import deque
from typing import List, Optional


class Solution:
    def largestValues(self, root: "Optional[TreeNode]") -> List[int]:
        pending = deque([root]) if root is not None else deque()
        result = []
        while pending:
            greatest = pending[0].val
            for _ in range(len(pending)):
                node = pending.popleft()
                greatest = max(greatest, node.val)
                if node.left is not None:
                    pending.append(node.left)
                if node.right is not None:
                    pending.append(node.right)
            result.append(greatest)
        return result

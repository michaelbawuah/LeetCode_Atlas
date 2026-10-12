from collections import deque
from typing import Optional


class Solution:
    def findBottomLeftValue(self, root: "Optional[TreeNode]") -> int:
        pending = deque([root])
        answer = root.val
        while pending:
            answer = pending[0].val
            for _ in range(len(pending)):
                node = pending.popleft()
                if node.left is not None:
                    pending.append(node.left)
                if node.right is not None:
                    pending.append(node.right)
        return answer

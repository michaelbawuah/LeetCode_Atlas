from collections import deque
from typing import Optional


class Solution:
    def widthOfBinaryTree(self, root: "Optional[TreeNode]") -> int:
        pending = deque([(root, 0)])
        widest = 0
        while pending:
            base = pending[0][1]
            width = 0
            for _ in range(len(pending)):
                node, position = pending.popleft()
                position -= base
                width = position + 1
                if node.left is not None:
                    pending.append((node.left, 2 * position))
                if node.right is not None:
                    pending.append((node.right, 2 * position + 1))
            widest = max(widest, width)
        return widest

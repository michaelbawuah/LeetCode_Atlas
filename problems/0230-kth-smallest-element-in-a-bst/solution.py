from typing import Optional


class Solution:
    def kthSmallest(self, root: "Optional[TreeNode]", k: int) -> int:
        stack = []
        current = root
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            current = current.right
        raise ValueError("k must identify an existing BST node")

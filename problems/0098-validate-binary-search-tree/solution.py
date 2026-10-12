from typing import Optional


class Solution:
    def isValidBST(self, root: "Optional[TreeNode]") -> bool:
        stack = []
        current = root
        previous = None
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if previous is not None and current.val <= previous:
                return False
            previous = current.val
            current = current.right
        return True

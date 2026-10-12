from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: "Optional[TreeNode]") -> List[int]:
        stack, values = [], []
        current = root
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            values.append(current.val)
            current = current.right
        return values

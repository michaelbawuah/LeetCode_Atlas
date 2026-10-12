from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: "Optional[TreeNode]") -> List[int]:
        values = []
        stack = [(root, False)] if root is not None else []
        while stack:
            node, ready = stack.pop()
            if ready:
                values.append(node.val)
            else:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
        return values

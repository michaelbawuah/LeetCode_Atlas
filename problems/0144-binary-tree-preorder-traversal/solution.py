from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: "Optional[TreeNode]") -> List[int]:
        if root is None:
            return []
        stack, values = [root], []
        while stack:
            node = stack.pop()
            values.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return values

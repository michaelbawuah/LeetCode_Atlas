from typing import Optional


class Solution:
    def flatten(self, root: "Optional[TreeNode]") -> None:
        stack = [root] if root is not None else []
        previous = None
        while stack:
            node = stack.pop()
            if previous is not None:
                previous.left = None
                previous.right = node
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            previous = node
        if previous is not None:
            previous.left = None
            previous.right = None

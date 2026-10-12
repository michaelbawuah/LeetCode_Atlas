from typing import Optional


class Solution:
    def isBalanced(self, root: "Optional[TreeNode]") -> bool:
        heights = {None: 0}
        stack = [(root, False)] if root is not None else []
        while stack:
            node, ready = stack.pop()
            if ready:
                left_height, right_height = heights[node.left], heights[node.right]
                if abs(left_height - right_height) > 1:
                    return False
                heights[node] = 1 + max(left_height, right_height)
            else:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
        return True

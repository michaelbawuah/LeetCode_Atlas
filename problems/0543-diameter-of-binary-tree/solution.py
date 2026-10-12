from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: "Optional[TreeNode]") -> int:
        heights = {None: 0}
        longest = 0
        stack = [(root, False)]
        while stack:
            node, ready = stack.pop()
            if ready:
                left, right = heights[node.left], heights[node.right]
                longest = max(longest, left + right)
                heights[node] = 1 + max(left, right)
            else:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
        return longest

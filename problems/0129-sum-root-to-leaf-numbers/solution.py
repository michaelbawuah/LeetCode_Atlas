from typing import Optional


class Solution:
    def sumNumbers(self, root: "Optional[TreeNode]") -> int:
        total = 0
        stack = [(root, 0)]
        while stack:
            node, prefix = stack.pop()
            number = prefix * 10 + node.val
            if node.left is None and node.right is None:
                total += number
            if node.right is not None:
                stack.append((node.right, number))
            if node.left is not None:
                stack.append((node.left, number))
        return total

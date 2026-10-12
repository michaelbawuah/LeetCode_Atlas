from typing import Optional


class Solution:
    def sumOfLeftLeaves(self, root: "Optional[TreeNode]") -> int:
        total = 0
        pending = [(root, False)]
        while pending:
            node, is_left = pending.pop()
            if is_left and node.left is None and node.right is None:
                total += node.val
            if node.right is not None:
                pending.append((node.right, False))
            if node.left is not None:
                pending.append((node.left, True))
        return total

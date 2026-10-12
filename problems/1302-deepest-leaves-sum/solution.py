from typing import Optional


class Solution:
    def deepestLeavesSum(self, root: "Optional[TreeNode]") -> int:
        deepest, total = 0, 0
        pending = [(root, 0)]
        while pending:
            node, depth = pending.pop()
            if depth > deepest:
                deepest, total = depth, node.val
            elif depth == deepest:
                total += node.val
            if node.right is not None:
                pending.append((node.right, depth + 1))
            if node.left is not None:
                pending.append((node.left, depth + 1))
        return total

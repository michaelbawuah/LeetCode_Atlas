from typing import Optional


class Solution:
    def rangeSumBST(self, root: "Optional[TreeNode]", low: int, high: int) -> int:
        total = 0
        pending = [root]
        while pending:
            node = pending.pop()
            if low <= node.val <= high:
                total += node.val
            if node.left is not None and node.val > low:
                pending.append(node.left)
            if node.right is not None and node.val < high:
                pending.append(node.right)
        return total

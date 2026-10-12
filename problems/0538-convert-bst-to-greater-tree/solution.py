from typing import Optional


class Solution:
    def convertBST(self, root: "Optional[TreeNode]") -> "Optional[TreeNode]":
        pending, current = [], root
        total = 0
        while pending or current is not None:
            while current is not None:
                pending.append(current)
                current = current.right
            current = pending.pop()
            total += current.val
            current.val = total
            current = current.left
        return root

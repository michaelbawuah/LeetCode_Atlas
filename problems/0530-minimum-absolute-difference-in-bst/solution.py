from typing import Optional


class Solution:
    def getMinimumDifference(self, root: "Optional[TreeNode]") -> int:
        pending, current = [], root
        previous = None
        best = float("inf")
        while pending or current is not None:
            while current is not None:
                pending.append(current)
                current = current.left
            current = pending.pop()
            if previous is not None:
                best = min(best, current.val - previous)
            previous = current.val
            current = current.right
        return int(best)

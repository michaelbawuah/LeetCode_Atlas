from typing import Optional


class Solution:
    def isSymmetric(self, root: "Optional[TreeNode]") -> bool:
        pending = [(root.left, root.right)]
        while pending:
            left, right = pending.pop()
            if left is None or right is None:
                if left is not right:
                    return False
                continue
            if left.val != right.val:
                return False
            pending.append((left.left, right.right))
            pending.append((left.right, right.left))
        return True

from typing import Optional


class Solution:
    def mergeTrees(
        self, root1: "Optional[TreeNode]", root2: "Optional[TreeNode]"
    ) -> "Optional[TreeNode]":
        if root1 is None and root2 is None:
            return None
        root = TreeNode(
            (root1.val if root1 is not None else 0) + (root2.val if root2 is not None else 0)
        )
        pending = [(root, root1, root2)]
        while pending:
            merged, first, second = pending.pop()
            for field in ("left", "right"):
                left = getattr(first, field) if first is not None else None
                right = getattr(second, field) if second is not None else None
                if left is None and right is None:
                    continue
                child = TreeNode(
                    (left.val if left is not None else 0) + (right.val if right is not None else 0)
                )
                setattr(merged, field, child)
                pending.append((child, left, right))
        return root

from typing import Optional


class Solution:
    def insertIntoBST(self, root: "Optional[TreeNode]", val: int) -> "Optional[TreeNode]":
        if root is None:
            return TreeNode(val)
        current = root
        while True:
            field = "left" if val < current.val else "right"
            child = getattr(current, field)
            if child is None:
                setattr(current, field, TreeNode(val))
                return root
            current = child

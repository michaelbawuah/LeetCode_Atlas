from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> "Optional[TreeNode]":
        root = None
        pending = [(0, len(nums), None, "")]
        while pending:
            low, high, parent, field = pending.pop()
            if low >= high:
                continue
            middle = low + (high - low) // 2
            node = TreeNode(nums[middle])
            if parent is None:
                root = node
            else:
                setattr(parent, field, node)
            pending.append((middle + 1, high, node, "right"))
            pending.append((low, middle, node, "left"))
        return root

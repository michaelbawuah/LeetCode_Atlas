from typing import List, Optional


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> "Optional[TreeNode]":
        pending = []
        for value in nums:
            node = TreeNode(value)
            while pending and pending[-1].val < value:
                node.left = pending.pop()
            if pending:
                pending[-1].right = node
            pending.append(node)
        return pending[0]

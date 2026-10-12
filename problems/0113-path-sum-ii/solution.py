from typing import List, Optional


class Solution:
    def pathSum(self, root: "Optional[TreeNode]", targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        results, path = [], []
        stack = [(root, 0, False)]
        while stack:
            node, total, leaving = stack.pop()
            if leaving:
                path.pop()
                continue
            total += node.val
            path.append(node.val)
            if node.left is None and node.right is None and total == targetSum:
                results.append(path.copy())
            stack.append((node, total, True))
            if node.right is not None:
                stack.append((node.right, total, False))
            if node.left is not None:
                stack.append((node.left, total, False))
        return results

from typing import Optional


class Solution:
    def countNodes(self, root: "Optional[TreeNode]") -> int:
        pending = [root] if root is not None else []
        total = 0
        while pending:
            node = pending.pop()
            left_height = right_height = 0
            left = right = node
            while left is not None:
                left_height += 1
                left = left.left
            while right is not None:
                right_height += 1
                right = right.right
            if left_height == right_height:
                total += (1 << left_height) - 1
            else:
                total += 1
                if node.right is not None:
                    pending.append(node.right)
                if node.left is not None:
                    pending.append(node.left)
        return total

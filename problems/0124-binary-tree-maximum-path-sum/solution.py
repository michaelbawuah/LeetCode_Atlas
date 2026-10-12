from typing import Optional


class Solution:
    def maxPathSum(self, root: "Optional[TreeNode]") -> int:
        gains = {None: 0}
        best = root.val
        stack = [(root, False)]
        while stack:
            node, ready = stack.pop()
            if ready:
                left, right = max(0, gains[node.left]), max(0, gains[node.right])
                best = max(best, node.val + left + right)
                gains[node] = node.val + max(left, right)
            else:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
        return best

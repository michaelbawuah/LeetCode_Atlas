from typing import List, Optional


class Solution:
    def rightSideView(self, root: "Optional[TreeNode]") -> List[int]:
        if root is None:
            return []
        view = []
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if depth == len(view):
                view.append(node.val)
            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))
        return view

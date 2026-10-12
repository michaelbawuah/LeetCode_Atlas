from typing import List, Optional


class Solution:
    def binaryTreePaths(self, root: "Optional[TreeNode]") -> List[str]:
        result, path = [], []
        pending = [(root, False)]
        while pending:
            node, leaving = pending.pop()
            if leaving:
                path.pop()
                continue
            path.append(str(node.val))
            if node.left is None and node.right is None:
                result.append("->".join(path))
            pending.append((node, True))
            if node.right is not None:
                pending.append((node.right, False))
            if node.left is not None:
                pending.append((node.left, False))
        return result

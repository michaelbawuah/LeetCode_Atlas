from typing import Optional


class Solution:
    def maxAncestorDiff(self, root: "Optional[TreeNode]") -> int:
        answer = 0
        pending = [(root, root.val, root.val)]
        while pending:
            node, minimum, maximum = pending.pop()
            minimum = min(minimum, node.val)
            maximum = max(maximum, node.val)
            answer = max(answer, maximum - minimum)
            if node.right is not None:
                pending.append((node.right, minimum, maximum))
            if node.left is not None:
                pending.append((node.left, minimum, maximum))
        return answer

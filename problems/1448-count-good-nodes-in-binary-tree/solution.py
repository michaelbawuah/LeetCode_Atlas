from typing import Optional


class Solution:
    def goodNodes(self, root: "Optional[TreeNode]") -> int:
        answer = 0
        pending = [(root, root.val)]
        while pending:
            node, greatest = pending.pop()
            if node.val >= greatest:
                answer += 1
            greatest = max(greatest, node.val)
            if node.right is not None:
                pending.append((node.right, greatest))
            if node.left is not None:
                pending.append((node.left, greatest))
        return answer

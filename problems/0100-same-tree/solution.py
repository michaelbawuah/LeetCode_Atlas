from typing import Optional


class Solution:
    def isSameTree(self, p: "Optional[TreeNode]", q: "Optional[TreeNode]") -> bool:
        stack = [(p, q)]
        while stack:
            first, second = stack.pop()
            if first is None or second is None:
                if first is not second:
                    return False
                continue
            if first.val != second.val:
                return False
            stack.append((first.left, second.left))
            stack.append((first.right, second.right))
        return True

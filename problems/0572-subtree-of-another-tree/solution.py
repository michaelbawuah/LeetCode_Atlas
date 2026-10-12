from typing import Optional


class Solution:
    def isSubtree(self, root: "Optional[TreeNode]", subRoot: "Optional[TreeNode]") -> bool:
        def matches(first, second):
            pairs = [(first, second)]
            while pairs:
                left, right = pairs.pop()
                if left is None or right is None:
                    if left is not right:
                        return False
                    continue
                if left.val != right.val:
                    return False
                pairs.append((left.left, right.left))
                pairs.append((left.right, right.right))
            return True

        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val and matches(node, subRoot):
                return True
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return False

from typing import Optional


class Solution:
    def pathSum(self, root: "Optional[TreeNode]", targetSum: int) -> int:
        prefixes = {0: 1}
        answer = 0
        pending = [(root, 0, False)] if root is not None else []
        while pending:
            node, prefix, leaving = pending.pop()
            if leaving:
                prefixes[prefix] -= 1
                if prefixes[prefix] == 0:
                    del prefixes[prefix]
                continue
            prefix += node.val
            answer += prefixes.get(prefix - targetSum, 0)
            prefixes[prefix] = prefixes.get(prefix, 0) + 1
            pending.append((node, prefix, True))
            if node.right is not None:
                pending.append((node.right, prefix, False))
            if node.left is not None:
                pending.append((node.left, prefix, False))
        return answer

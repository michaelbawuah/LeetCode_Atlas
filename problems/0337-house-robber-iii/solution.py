from typing import Optional


class Solution:
    def rob(self, root: "Optional[TreeNode]") -> int:
        outcomes = {None: (0, 0)}
        pending = [(root, False)]
        while pending:
            node, ready = pending.pop()
            if ready:
                left_take, left_skip = outcomes[node.left]
                right_take, right_skip = outcomes[node.right]
                outcomes[node] = (
                    node.val + left_skip + right_skip,
                    max(left_take, left_skip) + max(right_take, right_skip),
                )
            else:
                pending.append((node, True))
                if node.right is not None:
                    pending.append((node.right, False))
                if node.left is not None:
                    pending.append((node.left, False))
        return max(outcomes[root])

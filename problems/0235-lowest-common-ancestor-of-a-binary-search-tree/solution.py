class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        low, high = min(p.val, q.val), max(p.val, q.val)
        while root is not None:
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
            else:
                return root
        return None

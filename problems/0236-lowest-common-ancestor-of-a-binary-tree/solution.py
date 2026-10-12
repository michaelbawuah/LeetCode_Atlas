class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        parents = {root: None}
        pending = [root]
        while p not in parents or q not in parents:
            node = pending.pop()
            if node.left is not None:
                parents[node.left] = node
                pending.append(node.left)
            if node.right is not None:
                parents[node.right] = node
                pending.append(node.right)
        ancestors = set()
        current = p
        while current is not None:
            ancestors.add(current)
            current = parents[current]
        current = q
        while current not in ancestors:
            current = parents[current]
        return current

from typing import Optional


class Solution:
    def deleteNode(self, root: "Optional[TreeNode]", key: int) -> "Optional[TreeNode]":
        parent, node = None, root
        while node is not None and node.val != key:
            parent = node
            node = node.left if key < node.val else node.right
        if node is None:
            return root
        if node.left is None:
            replacement = node.right
        elif node.right is None:
            replacement = node.left
        else:
            successor_parent, successor = node, node.right
            while successor.left is not None:
                successor_parent, successor = successor, successor.left
            if successor_parent is not node:
                successor_parent.left = successor.right
                successor.right = node.right
            successor.left = node.left
            replacement = successor
        if parent is None:
            root = replacement
        elif parent.left is node:
            parent.left = replacement
        else:
            parent.right = replacement
        node.left = node.right = None
        return root

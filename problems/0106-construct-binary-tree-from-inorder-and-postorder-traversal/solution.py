from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> "Optional[TreeNode]":
        root = TreeNode(postorder[-1])
        stack = [root]
        inorder_index = len(inorder) - 1
        for index in range(len(postorder) - 2, -1, -1):
            value = postorder[index]
            child = TreeNode(value)
            if stack[-1].val != inorder[inorder_index]:
                stack[-1].right = child
            else:
                parent = stack.pop()
                inorder_index -= 1
                while stack and stack[-1].val == inorder[inorder_index]:
                    parent = stack.pop()
                    inorder_index -= 1
                parent.left = child
            stack.append(child)
        return root

from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> "Optional[TreeNode]":
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0
        for index in range(1, len(preorder)):
            value = preorder[index]
            child = TreeNode(value)
            if stack[-1].val != inorder[inorder_index]:
                stack[-1].left = child
            else:
                parent = stack.pop()
                inorder_index += 1
                while stack and stack[-1].val == inorder[inorder_index]:
                    parent = stack.pop()
                    inorder_index += 1
                parent.right = child
            stack.append(child)
        return root

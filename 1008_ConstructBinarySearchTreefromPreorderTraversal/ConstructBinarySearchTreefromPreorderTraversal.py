# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        stack = []
        for v in preorder:
            node = TreeNode(v)
            if not root: root = node
            elif v < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and stack[-1].val < v:
                    last = stack.pop()
                last.right = node
            stack.append(node)
        return root

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        for v in preorder:
            if not root: root = TreeNode(v)
            else: self.insert(root, v)
        return root
    
    def insert(self, root, v):
        if not root: return TreeNode(v)
        if root.val < v:
            root.right = self.insert(root.right, v)
        elif v < root.val:
            root.left = self.insert(root.left, v)
        return root
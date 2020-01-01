# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        left_height, right_height = self.maxDepth(root.left), self.maxDepth(root.right)
        return 1 + max(left_height, right_height)
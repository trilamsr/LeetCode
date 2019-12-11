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

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+ 1)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        stack = collections.deque([root])
        level = 0
        while stack:
            level += 1
            for i in range(len(stack)):
                cur = stack.popleft()
                if cur.left: stack.append(cur.left)
                if cur.right: stack.append(cur.right)
        return level


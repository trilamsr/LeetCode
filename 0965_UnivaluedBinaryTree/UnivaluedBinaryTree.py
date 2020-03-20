# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.dfs(root, root.val)
    
    def dfs(self, node, val):
        if not node: return True
        left = self.dfs(node.left, val)
        right = self.dfs(node.right, val)
        return left and right and node.val == val

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        queue = [root]
        val = root.val
        while queue:
            cur = queue.pop()
            if cur.val != val: return False
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
        return True
        
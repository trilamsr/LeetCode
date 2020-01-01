# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if not root.left and not root.right: return sum == root.val
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root and not sum: return False
        return self.recurse(root, 0, sum)
    
    def recurse(self, node, cur, sum):
        if not node: return False
        if cur + node.val == sum and not node.left and not node.right: return True
        return self.recurse(node.left, cur+node.val, sum) or self.recurse(node.right, cur+node.val, sum)
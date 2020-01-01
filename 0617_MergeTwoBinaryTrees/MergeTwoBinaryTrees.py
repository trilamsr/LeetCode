# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# In place
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2: return None
        if not t1 or not t2: return t1 or t2
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


# New Tree
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2: return None
        if not t1 or not t2:
            temp = t1 or t2
            ret = TreeNode(temp.val)
            ret.left = self.mergeTrees(temp.left, None)
            ret.right= self.mergeTrees(temp.right, None)
        else:
            ret = TreeNode(t1.val + t2.val)
            ret.left = self.mergeTrees(t1.left, t2.left)
            ret.right = self.mergeTrees(t1.right, t2.right)
        return ret
    
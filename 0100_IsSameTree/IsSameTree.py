# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        left = self.structure(p)
        right = self.structure(q)
        return left == right
    def structure(self, p: TreeNode):
        ret = []
        def helper (node):
            if (node == None):
                ret.append(0)
            else:
                ret.append(node.val)
                helper(node.left)
                helper(node.right)
        helper(p)
        return ret
        
class Solution2:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p == None and q == None):
            return True
        if (p == None or q == None):
            return False
        if (p.val != q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)




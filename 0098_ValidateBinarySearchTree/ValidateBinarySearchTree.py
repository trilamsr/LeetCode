# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, lo, hi):
            if not node: return True
            if valid(node.left, lo, node.val) and lo < node.val < hi:
                return valid(node.right, node.val, hi)
            return False
        return valid(root, float('-inf'), float('inf') )


class Solution:
    def predecessor(self, node):
        pred = node.left
        while pred.right and pred.right != node:
            pred = pred.right
        return pred
        
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True;
        cur = root
        min_val = float('-inf')
        while cur:
            if not cur.left:
                if cur.val <= min_val: return False
                min_val = cur.val
                cur = cur.right
            else:
                pred = self.predecessor(cur)
                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                else:
                    if cur.val <= min_val: return False
                    min_val = cur.val
                    cur = cur.right
                    pred.right = None
        return True
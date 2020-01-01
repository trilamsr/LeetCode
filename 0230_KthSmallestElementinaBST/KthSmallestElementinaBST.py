# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def populate_left_spine(spine, node):
    while node:
        spine.append(node)
        node = node.left
    
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        spine, node = [], root
        while node or spine:
            populate_left_spine(spine, node)
            node = spine.pop()
            k-=1
            if k == 0: return node.val
            node = node.right
            
        
            
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
​
​
# so given a tree -> we linearize it
#       5
#      /\ 
#     /\ \
#    /  \ \
#   /    \ \
#   ^    ^
#  1     4
#         root
#          v
# [1,2,3,4,5,6,7,8,9]

- so we ask...
- is 4 connected to 5?
    -> if its not... that means we're climbing down
    -> so connect 4 to 5
- 4 is connected to 5
    -> if it is connected: it means we came to 5 via 4
        -> set 4 -> None (autocorrecting)
'''

def is_connected(pred, node):
    return pred.right == node
​
# right most element of the left-subtree
def left_adjacent_neighbor(node):
    pred = node.left
    while pred.right and pred.right != node:
        pred = pred.right
    return pred
​
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        ret = []
        node = root
        
        while node:
            # since there is nothing to the left
            # try climbing down via the right
            if not node.left:
                ret.append(node.val)
                node = node.right
            else:
​
                pred = left_adjacent_neighbor(node)
                
                # this means we are climbing down
                if not is_connected(pred, node):
                    pred.right, node = node, node.left
                else:
                # is it is not connected -> it means we are climbing back up
                    ret.append(node.val)
                    pred.right, node = None, node.right
        return ret
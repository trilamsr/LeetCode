# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Morris

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        def recurse(node):
            if not node: return
            recurse(node.left)
            ret.append(node.val)
            recurse(node.right)
        recurse(root)
        return ret

class Solution:
    def predecessor(self, node):
        pred = node.left
        while pred.right and pred.right != node:
            pred = pred.right
        return pred
    
    def not_connected(self, pred, cur):
        return pred.right != cur
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        ret = []
        cur = root
        while cur:
            if not cur.left:
                ret.append(cur.val)
                cur = cur.right
            else:
                pred = self.predecessor(cur)
                # Climbing down
                if self.not_connected(pred, cur):
                # if not pred.right:
                    pred.right = cur
                    cur = cur.left
                # Climbing up
                else:
                    ret.append(cur.val)
                    cur = cur.right
                    pred.right = None
        return ret




def populate_leftspine(spine, node):
    while node:
        spine.append(node)
        node = node.left
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        spine, node = [], root
        while spine or node:
            # populate the left spine of the tree  with respect to current 'root'
            populate_leftspine(spine, node)
            # we are now at the bottom of the leftspine
            # we are now ready to climb back up
            node = spine.pop()
            ret.append(node.val)
            
            # if there is a right-subtree,
            # we take a detour and solve that
            # then we resume to climb back up our current spine
            # after that subproblem is solved
            node = node.right
                        
        return ret




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        def recurse(node):
            if not node: return
            ret.append(node.val)
            recurse(node.left)
            recurse(node.right)
        recurse(root)
        return ret


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        ret = []
        stack = [root]
        while stack:
            cur = stack.pop()
            ret.append(cur.val)
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
        return ret 

            # curr = stack.pop()
            # if not curr: continue
            # ret.append(curr.val)
            # stack.extend(adjacent(curr)[::-1])

class Solution:
    def predecessor(self, cur):
        pred = cur.left
        while pred.right and pred.right != cur:
            pred = pred.right
        return pred
        
    def not_connected(self, pred, cur):
        return pred.right != cur
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        ret = []
        cur = root
        while cur:
            if not cur.left:
                ret.append(cur.val)
                cur = cur.right
            else:
                pred = self.predecessor(cur)
                if self.not_connected(pred, cur):
                # if not pred.right:
                    ret.append(cur.val)
                    pred.right = cur
                    cur = cur.left
                else:
                    cur = cur.right
                    pred.right = None
        return ret
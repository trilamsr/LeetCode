# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return
        rank = {v: i for i,v in enumerate(inorder)}
        nodes = (TreeNode(v) for v in preorder) 
        root = next(nodes)
        stack = [root]
        for node in nodes:
            if rank[node.val] < rank[stack[-1].val]:
                stack[-1].left = node
            else:
                while stack and rank[node.val] > rank[stack[-1].val]:
                    last = stack.pop()
                last.right = node
            stack.append(node)
        return root
        
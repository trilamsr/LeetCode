# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return
        self.nodes = (TreeNode(v) for v in preorder)
        self.rank = {v: i for i,v in enumerate(inorder)}
        return self.dfs(preorder, 0, len(inorder))
    
    def dfs(self, preorder, lo, hi):
        if lo == hi: return
        node = next(self.nodes)
        index = self.rank[node.val]
        node.left = self.dfs(preorder, lo, index)
        node.right = self.dfs(preorder, index+1, hi)
        return node

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
        
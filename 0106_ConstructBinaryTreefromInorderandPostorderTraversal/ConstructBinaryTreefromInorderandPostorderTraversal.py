class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return None
        root = TreeNode(postorder.pop())
        rank = {v:i for i, v in enumerate(inorder)}
        stack = [root]
        while postorder:
            node = TreeNode(postorder.pop())
            if rank[node.val] > rank[stack[-1].val]:
                stack[-1].right = node
            else:
                while stack and rank[node.val] < rank[stack[-1].val]:
                    succ = stack.pop()
                succ.left = node
            stack.append(node)
        return root

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        rank = {v:i for i, v in enumerate(inorder)}
        return self.dfs(postorder, 0, len(inorder), rank)
    
    def dfs(self, postorder, lo, hi, rank):
        if lo == hi: return None
        node = TreeNode(postorder.pop())
        index = rank[node.val]
        node.right = self.dfs(postorder, index +1, hi, rank)
        node.left = self.dfs(postorder, lo, index, rank)
        return node
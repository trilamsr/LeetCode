# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
    
    def dfs(self, root, p, q):
        if root in (root, p, q): return root
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if left and right: return root
        return left or right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        parents = self.find_parents(root, p, q)
        return self.find_lca(parents, p, q)
    
    def find_lca(self,parents, p, q):
        ancestor = set()
        while p:
            ancestor.add(p)
            p = parents[p]
        while q not in ancestor:
            q = parents[q]
        return q
        
    def find_parents(self,root, p, q):
        stack = [root]
        parents = {root: None}
        while p not in parents or q not in parents:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
                parents[cur.left] = cur
            if cur.right:
                stack.append(cur.right)
                parents[cur.right] = cur
        return parents    

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # BuildingHeap
        heap = [root]
        curI = 0
        pAddress = -1
        qAddress = -1
        while pAddress == -1 or qAddress == -1:
            if heap[curI] == p: pAddress = curI
            if heap[curI] == q: qAddress = curI
            leftI = curI*2+1
            rightI= curI*2+2
            while len(heap) < rightI+1:
                heap.append(None)
            if heap[curI] != None:
                print(heap[curI].val)
                if heap[curI].left: heap[leftI] = heap[curI].left
                if heap[curI].right: heap[rightI] = heap[curI].right
            curI+=1
        # ID Parent
        while pAddress != qAddress:
            if pAddress < qAddress: qAddress = (qAddress-1)//2
            if pAddress > qAddress: pAddress = (pAddress-1)//2
        return heap[pAddress]
        
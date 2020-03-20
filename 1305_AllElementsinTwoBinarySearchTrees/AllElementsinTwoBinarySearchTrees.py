# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from heapq import heappush, heappop
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        heap, ret = [], []
        self.add(root1, heap)
        self.add(root2, heap)
        while heap:
            ret.append(heappop(heap))
        return ret
    
    def add(self, node, heap):
        if not node: return
        heappush(heap, node.val)
        self.add(node.left, heap)
        self.add(node.right, heap)


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ret, a, b = [], [], []
        self.add(root1, a)
        self.add(root2, b)
        return self.merge(a, b)
    
    def merge(self, a,b):
        lo, hi, ret = 0, 0, []
        while lo < len(a) and hi < len(b):
            if a[lo] < b[hi]:
                ret.append(a[lo])
                lo += 1
            else:
                ret.append(b[hi])
                hi += 1
        ret.extend(a[lo:])
        ret.extend(b[hi:])
        return ret
        
    def add(self, node, mem):
        if not node: return
        self.add(node.left, mem)
        mem.append(node.val)
        self.add(node.right, mem)

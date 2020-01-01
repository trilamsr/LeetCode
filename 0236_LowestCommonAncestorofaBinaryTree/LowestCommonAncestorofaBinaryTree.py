# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
        
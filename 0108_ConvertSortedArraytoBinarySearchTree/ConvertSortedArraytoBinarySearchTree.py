# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[0:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        return self.recurse(0, len(nums)-1, nums)
        
    def recurse(self, lo, hi, nums):
        mid = lo+(hi-lo)//2
        if lo > hi: return None
        node = TreeNode(nums[mid])
        node.left = self.recurse(lo, mid-1, nums)
        node.right = self.recurse(mid+1, hi, nums)
        return node    
    
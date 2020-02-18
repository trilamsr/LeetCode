class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        lca_child = self.find_lca_child(nums)

        # If we're at the rightmost leaf: return to left most
        if lca_child < 0:
            self.reverse(nums, 0, n-1)
            return

        # Optimization 1:
        #   if we're at the left leaf, we can simply swap the last two element 
        if lca_child == n-2:
            self.swap(nums, n-1, n-2)
            return
        
        self.reverse(nums, lca_child+1, n-1)
        prop = lambda x: nums[x] > nums[lca_child]
        next_gt = self.search(lca_child+1, n-1, prop)
        self.swap(nums, lca_child, next_gt)
    
    def reverse(self, nums, lo, hi):
        while lo < hi:
            self.swap(nums, lo, hi)
            lo += 1
            hi -= 1
    
    def swap(self, arr, lo, hi):
        arr[hi], arr[lo] = arr[lo], arr[hi]
    
    def find_lca_child(self, nums):
        end = len(nums)-2
        while end >= 0 and nums[end] >= nums[end+1]:
            end -= 1
        return end
    
    def search(self, lo, hi, prop):
        while lo <= hi:
            mid = (lo+hi)//2
            if prop(mid):
                hi = mid-1
            else:
                lo = mid+1
        return lo
        
        
        
        
        
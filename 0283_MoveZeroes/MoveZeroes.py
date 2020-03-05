def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        self.partition(nums, 0, len(nums)-1)
        
    def partition(self, nums, lo, hi):
        ind = lo
        while ind <= hi:
            if nums[ind] != 0:
                swap(nums, ind, lo)
                ind += 1
                lo += 1
            else:
                 ind += 1
        

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lo = 0
        for hi in range(len(nums)):
            if nums[hi] != 0:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo +=1
                
                
class Solution:            
    def moveZeroes(self, nums: List[int]) -> None:
        size = 0
        for i, v in enumerate(nums):
            if v == 0: size += 1
            else:
                nums[i], nums[i-size] = nums[i-size], nums[i]
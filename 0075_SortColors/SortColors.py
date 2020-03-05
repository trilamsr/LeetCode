class Solution:
    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]
    
    def sortColors(self, nums: List[int]) -> None:
        self.partition(0, len(nums)-1, 1, nums)
        
    def partition(self, lo, hi, pivot, nums):
        ind = lo
        while ind <= hi:
            if nums[ind] < pivot:
                self.swap(nums, ind, lo)
                lo += 1
                ind += 1
            elif nums[ind] > pivot:
                self.swap(nums, ind, hi)
                hi -= 1
            else:
                ind += 1

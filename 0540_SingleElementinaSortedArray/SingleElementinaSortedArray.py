class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            ret = ret^num
        return ret


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        return self.binary_s(nums, self.key)
    
    def binary_s(self, nums, key):
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if self.key(mid, nums):
                hi = mid - 1
            else:
                lo = mid + 1
        return nums[lo-1]
    
    def key_1(self, mid, arr):
        if mid%2 != 0: mid += 1
        return arr[mid-1] == arr[mid]

    def key_2(self, mid, nums):
        if mid != 0 and nums[mid] != nums[mid-1]:
            mid -= 1
        n = len(nums) - 1
        return (n-mid) % 2 == 0


        
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (hi+lo)//2
            if mid == len(nums)-1 or nums[mid+1] < nums[mid]:
                hi = mid-1
            else:
                lo = mid+1
        return lo

def lower_bound(nums, property):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if property(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        is_decreasing = lambda x: x == len(nums) -1  or (nums[x+1] - nums[x] < 0)
        return lower_bound(nums, is_decreasing)
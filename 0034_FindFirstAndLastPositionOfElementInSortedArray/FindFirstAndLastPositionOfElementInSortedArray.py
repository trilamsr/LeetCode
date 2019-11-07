class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        GTE = lambda x: target <= nums[x]
        LTE = lambda x: target >= nums[x]
        lo = lower_bound(nums, target, GTE)
        hi = upper_bound(nums, target, LTE)
        return [lo, hi] if lo <= hi else [-1,-1]
        
def lower_bound (nums, target, prop):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if prop(mid):
            hi = mid-1
        else:
            lo = mid+1
    return lo

def upper_bound(nums, target, prop):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if prop(mid):
            lo = mid +1
        else:
            hi = mid-1
    return hi
            
                
        
        

def lower_bound(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = lower_bound(nums, target)
        hi = lower_bound(nums, target + 1) - 1
        return [lo, hi] if lo <= hi else [-1, -1]

'''
small optimization:
[5,7,7,8,8,10]; find 8
​
so we found lower_bound and got 3
[5,7,7,8,8,10]
       ^

on our next binary search: we can start from [3] instead of [0]
[5,7,7,8,8,10]
        ^---^
        start from here
# but this is still O(log(N))
# example: [8,8,8,8,8,8,8,8,8,8,8,8,9]
            ^(start here on the 2nd iteration), but still small optimization
​
​
def lower_bound(nums, lo, target):
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo
​
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = lower_bound(nums, 0, target)
        hi = lower_bound(nums, lo, target + 1) - 1
        return [lo, hi] if lo <= hi else [-1, -1]
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        minInd = self.MinIndex(nums)
        if nums[minInd] <= target <= nums[-1]:
            return self.find(nums, target, minInd, len(nums)-1)
        return self.find(nums, target, 0, minInd-1)
        
    def MinIndex(self, nums):
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] <= nums[-1]:
                hi = mid-1
            else:
                lo = mid+1
        return lo
    
    def find (self, nums, target, beg, end):
        while beg <= end:
            mid = (beg+end)//2
            if target == nums[mid]: return mid
            if target < nums[mid]:
                end = mid-1
            else:
                beg = mid+1
        return -1





def lower_bound(nums, lo, hi, property):
    while lo <= hi:
        mid = (lo + hi) // 2
        if property(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        
        less_than_eq = lambda x: nums[x] <= nums[-1]
        greater_than_eq = lambda x: nums[x] >= target
        
        min_idx = lower_bound(nums, 0, len(nums)-1, less_than_eq)
        is_rotated_side = nums[min_idx] <= target <= nums[-1]
        lo, hi = (min_idx, len(nums)-1) if is_rotated_side else (0, min_idx-1)
        
        ret = lower_bound(nums, lo, hi, greater_than_eq)
        return [-1, ret][nums[ret] == target]
        # return ret if nums[ret] == target else -1



# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if not nums: return -1
#         lo, hi = 0, len(nums) - 1
#         while lo <= hi:
#             mid = (lo + hi) // 2

#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] <= nums[hi]:
#                 if nums[mid] <= target <= nums[hi]:
#                     lo = mid + 1
#                 else:
#                     hi = mid - 1
#             else:
#                 if nums[lo] <= target <= nums[mid]:
#                     hi = mid - 1
#                 else:
#                     lo = mid + 1
#         return -1
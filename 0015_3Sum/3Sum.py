class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            self.explore(nums, ret, i)
        return ret
    
    def explore(self, nums, ret, i):
        lo, hi = i+1, len(nums)-1
        while lo < hi:
            child = (nums[lo], nums[hi], nums[i])
            total = sum(child)
            if total > 0: hi -= 1
            elif total < 0: lo += 1
            else:
                ret.append(child)
                while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                lo, hi = lo + 1, hi - 1

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()
        trail = set()
        for i, v in enumerate(nums):
            self.explore(i, v, nums, trail, ret)
            trail.add(v)
        return ret
    
    def explore(self, i, val, nums, trail, ret):
        for i in range(i+1, len(nums)):
            target = -(nums[i]+val)
            if target in trail:
                ret.add((target, nums[i], val))

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()
        for i in range(len(nums)):
            target = nums[i]
            self.explore(nums, ret, target, i)
        return ret
    
    def explore(self, nums, ret, target, i):
        left, right = i-1, i+1
        while 0 <= left and right < len(nums):
            total = nums[left] + nums[right] + target
            if total > 0: left -= 1
            elif total < 0: right += 1
            else:
                ret.add((nums[left], nums[right], target))
                left -= 1
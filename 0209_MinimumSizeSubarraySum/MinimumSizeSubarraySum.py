from math import inf

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        left = cur_sum = 0
        ret = inf
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= s:
                ret = min(right-left+1, ret)
                cur_sum -= nums[left]
                left += 1
        if ret == inf: return 0
        return ret

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        ret = inf
        sums = self.prefix_sums(nums)
        for start, prefix in enumerate(sums):
            target = s + prefix
            end = self.lower_bound(nums, lambda x: sums[x] >= target)
            if end != len(sums): 
                ret = min(ret, end-start)
        return ret if ret != inf else 0

    def prefix_sums(self, nums):
        ret = [0]
        for num in nums:
            ret.append(num+ret[-1])
        return ret

    def lower_bound(self, nums, prop):
        lo, hi = 0, len(nums)
        while lo <= hi:
            mid = (lo+hi)//2
            if prop(mid):
                hi = mid-1
            else:
                lo = mid+1
        return lo
    





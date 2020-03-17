import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_sub = min_sub = 1 
        ret = -math.inf
        for num in nums:
            candidates = (num, num*min_sub, num*max_sub)
            max_sub = max(*candidates)
            min_sub = min(*candidates)
            ret = max(ret, max_sub)
        return ret

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        n, ret = len(nums), -math.inf
        dp = [0]*n
        for size in range(n):
            cur_dp = [0]*n
            for i in range(size, len(nums)):
                past_product = dp[i-1] if size > 0 else 1
                cur_dp[i] = past_product*nums[i]
                ret = max(cur_dp[i], ret)
            dp = cur_dp
        return ret

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        n, ret = len(nums), -math.inf
        dp = [[0]*n for _ in range(n)]
        for size in range(n):
            for i in range(size, len(nums)):
                past_product = dp[size-1][i-1] if size > 0 else 1
                dp[size][i] = past_product*nums[i]
                ret = max(dp[size][i], ret)
        return ret
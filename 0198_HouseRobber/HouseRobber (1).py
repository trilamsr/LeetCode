class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [0]*len(nums)
        for i in range(len(nums)):
            print(dp[i-2])
            if i < 1: dp[i] = nums[i]
            else:
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        ret = nums[0]
        two_houses_ago_opt = 0
        for i in range(1, len(nums)):
            rob_opt = nums[i] + two_houses_ago_opt
            skip_opt = ret
            optimal = max(rob_opt, skip_opt)
            two_houses_ago_opt = ret
            ret = optimal            
        return ret
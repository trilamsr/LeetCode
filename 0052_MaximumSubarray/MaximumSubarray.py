class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        ret = float("-inf")
        cur_total = 0
        for delta in nums:
            cur_total = max(cur_total + delta, delta)
            ret = max(cur_total, ret)
        return ret
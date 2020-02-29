class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1]*len(nums)
        pre, post = 1, 1
        n = len(nums)
        for i in range(0, len(nums)):
            ret[i] *= pre
            ret[n-1-i] *= post
            pre *= nums[i]
            post *= nums[n-1-i]
        return ret

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1]*len(nums)
        cur_val = 1
        for i in range(1, len(nums)):
            ret[i] = nums[i-1]*ret[i-1]
        for i in range(len(ret)-1, -1, -1):
            ret[i] = ret[i]*cur_val
            cur_val *= nums[i]
        return ret
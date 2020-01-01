class Solution:
    def missingNumber(self, nums):
        ret = 0
        for i in range(len(nums)):
            ret ^= i+1 ^ nums[i]
        return ret

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums)*(len(nums)+1))//2 - sum(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxx = len(nums)+1
        mem = set(nums)
        for i in range(maxx):
            if i not in mem: return i




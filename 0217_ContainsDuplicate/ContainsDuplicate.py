class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: return True
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = {}
        for num in nums:
            if num in mem: return True
            mem[num] = True
        return False
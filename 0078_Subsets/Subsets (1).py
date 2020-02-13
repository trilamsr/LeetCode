# Bitwise improved
class Solution:
    def __init__(self):
        self.flags = [0xFFFF, 0xFF, 0xF, 0x3, 0x1]
    
    def get_index(self, num, limit):
        while num:
            trail = self.trailing_zeroes(num)
            if trail != limit:
                yield trail
            num &= num-1
    
    def trailing_zeroes(self, num):
        if num & 1: return 0
        ret = 0
        for i, flag in enumerate(self.flags):
            if not num & flag:
                ret  += 1<<(len(self.flags)-i-1)
                num >>= 1<<(len(self.flags)-i-1)
        return ret
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in range(1<<len(nums)):
            subset = []
            for ind in self.get_index(i, len(nums)):
                subset.append(nums[ind])
            ret.append(subset)
        return ret

# Tricks
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for num in nums:
            ret.extend([item+[num] for item in ret])
        return ret

# DFS
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        subset = []
        self.dfs(nums, subset, ret, 0)
        return ret
    
    def dfs(self, nums, subset, ret, index):
        ret.append(subset[:])
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, subset, ret, i+1)
            subset.pop()

# Bitwise not improved
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        for i in range(1<<len(nums)):
            cur_set = []
            for j in range(len(nums)):
                if i&(1<<j) > 0: cur_set.append(nums[j])
            ret.append(cur_set)
        return ret
                
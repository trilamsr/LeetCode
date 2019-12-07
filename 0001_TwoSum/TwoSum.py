from typing import List
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		mem = {}
		for i,v in enumerate(nums):
			if (v in mem):
				return [mem[v], i]
			mem[target-v] = i

aloha = Solution()
print(aloha.twoSum([2, 7, 11, 15], 9))



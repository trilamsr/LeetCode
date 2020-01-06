class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        large, small = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(large[0] * large[1] * large[2], small[0] * small[1] * large[0])

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])


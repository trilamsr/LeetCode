class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        nums[:] = nums[-k:]+nums[:-k]

class Solution:
    def reverse(self, liz, start, end):
        while start < end:
            liz[start], liz[end] = liz[end], liz[start]
            start += 1
            end -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)        
    
class Solution:
    def rotate(self, nums, k):
        d = collections.deque(nums)
        d.rotate(k)
        nums[:] = list(d)
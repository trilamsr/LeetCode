class Window():
    def __init__(self, nums, k):
        self.lo = 0
        self.hi = 0
        self.val = 0
        self.product = 1
        self.k = k
        self.nums = nums
    
    @property
    def satisfy(self):
        return not (self.lo <= self.hi and self.product >= self.k)
    
    def add(self):
        self.product *= self.nums[self.hi]
        
    def update(self):
        self.val += self.hi - self.lo + 1
        self.hi += 1
    
    def pop(self):
        self.product /= self.nums[self.lo]
        self.lo += 1
        
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        window = Window(nums, k)
        for num in nums:
            window.add()
            while not window.satisfy:
                window.pop()
            window.update()
        return window.val
    
    
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ret = 0
        left = 0
        product = 1
        for right, val in enumerate(nums):
            product *= val
            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            ret += right-left+1
        return ret

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        window = collections.deque()
        ret = 0
        product = 1
        for num in nums:
            window.append(num)
            product *= num
            while window and product >= k:
                product /= window.popleft()
            ret += len(window)
        return ret
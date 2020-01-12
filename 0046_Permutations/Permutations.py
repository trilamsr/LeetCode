class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        queue = [([nums[i]], 1<<i) for i in range(len(nums))]
        while queue:
            cur, state = queue.pop()
            if state == (1<<len(nums))-1:
                ret.append(cur)
            else:
                for i in range(len(nums)):
                    if state & 1<<i > 0: continue
                    queue.append((cur+[nums[i]], 1<<i|state))
        return ret

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(collections.deque(nums), [], ret)
        return ret
        
    def dfs(self, nums, stack, ret):
        if not nums:
            ret.append(stack[:])
            return
        for i in range(len(nums)):
            stack.append(nums.pop())
            self.dfs(nums, stack, ret)
            nums.appendleft(stack.pop())
        

# m_brax
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        ret = []
        
        def dfs(index):
            if index == len(nums):
                ret.append(nums[:])
                return
            for i in range(index, len(nums)):
                swap(nums, index, i)
                dfs(index + 1)
                swap(nums, index, i)
                
        def swap(A, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        dfs(0)
        return ret
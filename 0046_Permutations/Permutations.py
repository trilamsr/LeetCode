class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        ret = []
        
        def dfs(index):
            if index == len(nums):
                ret.append(nums[:])
                return
            for i in range(index, len(nums)):
                self.swap(nums, index, i)
                dfs(index + 1)
                self.swap(nums, index, i)
                
        dfs(0)
        return ret
    
    def swap(self, A, i, j):
        A[i], A[j] = A[j], A[i]
        
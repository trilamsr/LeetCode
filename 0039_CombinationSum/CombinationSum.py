class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack, ret = [], []
        self.dfs(candidates, stack, target, ret, 0, 0)
        return ret
    
    def dfs(self, candidates, stack, target, ret, start, total):
        if total > target: return
        if total == target:
            ret.append(copy.deepcopy(stack))
            return
        for i in range(start, len(candidates)):
            stack.append(candidates[i])
            self.dfs(candidates, stack, target, ret, i, total+candidates[i])
            stack.pop()
        return
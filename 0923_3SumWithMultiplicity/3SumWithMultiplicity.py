class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        ret = 0
        nums = sorted(list(set(A)))
        mod = 10**9+7
        frequency = collections.Counter(A)
        for i in range(len(nums)):
            j, k = i, len(nums)-1
            while j <= k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    ret += self.count(frequency, nums[i], nums[j], nums[k])
                if total > target or total == target: k -= 1
                if total < target or total == target: j += 1
        return ret%mod
    
    def count(self, frequency, a,b,c):
        if a == b == c:
            nC3 = ((frequency[a]-2) * (frequency[a]-1) * frequency[a])//6
            return nC3
        if a == b or b == c:
            if a == b: return (frequency[a]*(frequency[b]-1))//2*frequency[c]
            if b == c: return (frequency[c]*(frequency[b]-1))//2*frequency[a]
        return frequency[a]*frequency[b]*frequency[c]
            

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        ret = 0
        for i in range(len(A)-2):
            for j in range(i+1, len(A)-1):
                for k in range(j+1, len(A)):
                    total = A[i] + A[j] + A[k]
                    if total == target: ret += 1
        return ret


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        ret = collections.defaultdict(int)
        stack = []
        self.dfs(0, A, stack, target, ret)
        return sum(ret.values())
    
    def dfs(self, start, A, stack, target, ret):
        if len(stack) == 3:
            if sum(stack) == target:
                ret[tuple(stack)] += 1
            return
        for i in range(start, len(A)):
            stack.append(A[i])
            self.dfs(i+1, A, stack, target, ret)
            stack.pop()
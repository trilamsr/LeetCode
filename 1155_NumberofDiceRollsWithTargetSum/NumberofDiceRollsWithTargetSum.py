class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for roll in range(d):
            next_window = [0]*(target+1)
            for node in range(target+1):
                for val in range(1, f+1):
                    if node+val >= target+1: break
                    next_window[node+val] += dp[node]
            dp = next_window
        divisor = 10**9+7
        return dp[target] % divisor

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 10**9+7
        dp = [[0]*(target+1) for _ in range(d+1)]
        dp[0][0] = 1
        for roll in range(d):
            for t in range(target+1):
                for face in range(1, f+1):
                    if t+face >= target+1: break
                    dp[roll+1][t+face] += dp[roll][t]
        return dp[d][target] % modulo

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo, modulo = {}, 10**9+7
        ret = self.top_down(d, f, target, memo) 
        return ret % modulo
    
    def top_down(self, count, faces, target, memo):
        if (count,target) in memo: return memo[(count,target)]
        if count == 0: return 1 if target == 0 else 0
        if target < 0: return 0
        ret = 0
        for face in range(1, faces+1):
            ret += self.top_down(count-1, faces, target-face, memo)
        memo[(count,target)] = ret
        return memo[(count,target)]
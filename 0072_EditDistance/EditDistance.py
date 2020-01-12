class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1)+1, len(word2)+1
        dp = [i for i in range(n)]
        for i in range(m):
            cur_dp = [k for k in range(i, i+n)]
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    cur_dp[j] = dp[j-1]
                else:
                    op1 = dp[j]
                    op2 = cur_dp[j-1]
                    op3 = dp[j-1]
                    cur_dp[j] = 1 + min(op1,op2,op3)
            dp = cur_dp
        return dp[n-1]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1)+1, len(word2)+1
        dp = [[0]*(n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not i or not j:
                    if i == 0: dp[i][j] = j
                    if j == 0: dp[i][j] = i
                    continue
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    op1 = dp[i-1][j]
                    op2 = dp[i][j-1]
                    op3 = dp[i-1][j-1]
                    dp[i][j] = 1 + min(op1,op2,op3)
        return dp[m-1][n-1]
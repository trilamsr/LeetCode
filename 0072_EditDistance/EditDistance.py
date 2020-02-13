class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1)+1, len(word2)+1
        dp = [0]*n
        for i in range(m):
            cur_dp = [k for k in range(i, n+i)]
            for j in range(n):
                if j == 0 or i == 0: continue
                if word1[i-1] == word2[j-1]:
                    cur_dp[j] = dp[j-1]
                else:
                    remove = dp[j]
                    replace = dp[j-1]
                    add = cur_dp[j-1]
                    cur_dp[j] = 1+min(remove, replace, add)
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
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    remove = dp[i-1][j]
                    add = dp[i][j-1]
                    replace = dp[i-1][j-1]
                    dp[i][j] = 1 + min(remove,replace,add)
        return dp[m-1][n-1]
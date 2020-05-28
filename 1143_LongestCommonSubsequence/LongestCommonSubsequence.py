class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        m, n = len(text1)+1, len(text2)+1
        dp = [[0]*n for _ in range(m)]
        for i, char1 in enumerate(text1):
            for j, char2 in enumerate(text2):
                if char1 == char2:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        return self.dfs(memo, text1, text2, 0, 0)
    
    def dfs(self, memo, word1, word2, i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(word1) or j == len(word2):
            return 0
        if word1[i] == word2[j]:
            memo[(i, j)] = 1 + self.dfs(memo, word1, word2, i+1, j+1)
        else:
            move_i = self.dfs(memo, word1, word2, i+1, j)
            move_j = self.dfs(memo, word1, word2, i, j+1)
            memo[(i, j)] = max(move_i, move_j)
        return memo[(i, j)]
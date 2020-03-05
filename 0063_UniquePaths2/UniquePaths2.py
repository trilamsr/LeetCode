# No Space - potential integer overflow
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n  = len(obstacleGrid), len(obstacleGrid[0])
        start = obstacleGrid[0][0]
        if start == 1: return 0
        for i in range(m):
            for j in range(n):
                obstacleGrid[i][j] = self.get_val(obstacleGrid, i, j)
        return obstacleGrid[m-1][n-1]
    
    def get_val(self, grid, i, j):
        if not i and not j: return 1
        if grid[i][j] == 1: return 0
        if not i: return grid[i][j-1]
        if not j: return grid[i-1][j]
        top = grid[i-1][j]
        left = grid[i][j-1]
        return top+left

# Space m*n - potential integer overflow
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n  = len(obstacleGrid), len(obstacleGrid[0])
        start = obstacleGrid[0][0]
        if start == 1: return 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = self.get_val(obstacleGrid, dp, i, j)
        return dp[m-1][n-1]
    
    def get_val(self, grid, dp, i, j):
        if not i and not j: return 1
        if grid[i][j] == 1: return 0
        if not i: return dp[i][j-1]
        if not j: return dp[i-1][j]
        top = dp[i-1][j]
        left = dp[i][j-1]
        return top+left
            
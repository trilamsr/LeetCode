import itertools
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        val = lambda y,x : grid[y][x] if 0 <= y < m and 0 <= x < n else math.inf
        for i, j in self.grid_2d(grid):
            if i == 0 and j == 0: continue
            top  = val(i-1, j)
            left = val(i, j-1)
            grid[i][j] = val(i, j) + min(top, left)
        return grid[m-1][n-1]
        
    def grid_2d(self, grid):
        m, n = len(grid), len(grid[0])
        return itertools.product(range(m), range(n))


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        return self.dfs(grid, 0, 0, m-1, n-1, memo)
    
    def dfs(self, grid, i, j, target_i, target_j, memo):
        if (i, j) in memo: return memo[(i, j)]
        if i == target_i and j == target_j:
            return grid[i][j]
        down = right = math.inf
        val = grid[i][j]
        if i < target_i:
            down = self.dfs(grid, i+1, j, target_i, target_j, memo)
        if j < target_j:
            right = self.dfs(grid, i, j+1, target_i, target_j, memo)
        memo[(i, j)] = val + min(down, right)
        return memo[(i, j)]
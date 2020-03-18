class Solution:
    def __init__(self):
        self.directions = [(-1,0),(1,0),(0,-1),(0,1)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ret = 0
        for i in range(m):
            for j in range(n):
                count = self.explore(grid, i, j)
                ret = max(ret, count)
        return ret
    
    def explore(self, grid, i, j):
        if grid[i][j] == 0: return 0
        grid[i][j] = 0
        ret = 1
        for y, x in self.valid_neighbor(grid, i, j):
            ret += self.explore(grid, y, x)
        return ret
    
    def valid_neighbor(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        for di, dj in self.directions:
            if not (0 <= i+di < m) or not (0<= j+dj< n): continue
            yield i+di, j+dj


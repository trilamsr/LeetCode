from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue, visited = deque([(0,0, k, 0)]), set()
        while queue:
            x, y, r, step = queue.popleft()
            if (x,y) == (m-1, n-1): return step
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny, nr = x+dx, y+dy, r-grid[x][y]
                if not 0 <= nx < len(grid) or not 0 <= ny < len(grid[0]): continue
                if (nx,ny,nr) in visited or nr < 0: continue
                visited.add((nx, ny, nr))
                queue.append((nx,ny,nr, step+1))
        return -1
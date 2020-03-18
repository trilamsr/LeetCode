import heapq
from itertools import cycle
from collections import deque

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0]*n for _ in range(n)]
        row, col = len(ret), len(ret[0])
        i, j, di, dj = 0, -1, 0, 1
        directions = cycle([(1, 0), (0, -1), (-1, 0), (0, 1)])
        valid = lambda y, x: 0 <= y < row and 0 <= x < row and ret[y][x] == 0
        for num in range(1, n*n+1):
            if not valid(i+di, j+dj):
                di, dj = next(directions)
            i, j = i + di, j + dj                
            ret[i][j] = num
        return ret

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0]*n for _ in range(n)]
        start = 1
        for i, j in self.spiral_iterator(ret):
            ret[i][j] = start
            start += 1
        return ret
    
    def magnitude(self, row, col):
        yield col
        yield row - 1
        no_overlap = row > 1 and col > 1
        if no_overlap:
            yield col - 1
            yield row - 2
    
    def spiral_iterator(self, grid):
        row, col = len(grid), len(grid[0])
        ring_count = (min(row, col)+1)//2
        directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
        i, j = 0, -1
        for _ in range(ring_count):
            for magnitude in self.magnitude(row, col):
                di, dj = next(directions)
                for _ in range(magnitude):
                    i, j = i + di, j + dj
                    yield i, j
            row, col = row-2, col-2

            
            
            
            
            
            
            
            
            
        
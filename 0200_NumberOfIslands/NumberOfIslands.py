def flip(grid, row, col):
    is_inbound = (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
    if not is_inbound: return
    if grid[row][col]  == '0': return
    grid[row][col] = '0'
    flip(grid, row-1, col)
    flip(grid, row+1, col)
    flip(grid, row, col-1)
    flip(grid, row, col+1)
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    flip(grid, row, col)
                    ret += 1
        return ret

# ------------------------------------------------

DIRS = [(1, 0),(-1, 0),(0, -1),(0, 1)]

def adjacent(grid, row, col):
    num_rows, num_cols = len(grid), len(grid[0])
    for i, j in DIRS:
        ri, cj = row + i, col + j
        is_inbound = (0 <= ri < num_rows) and (0 <= cj < num_cols)
        if is_inbound and grid[ri][cj] == '1':
            yield ri, cj

def adjacent(grid, row, col):
    num_rows, num_cols = len(grid), len(grid[0])
    if row - 1 >= 0: yield row - 1, col
    if row + 1 < num_rows: yield row + 1, col
    if col - 1 >= 0: yield row, col - 1
    if col + 1 < num_cols: yield row, col + 1
        
def dfs(grid, row, col):
    if grid[row][col] == '0':
        return 0
    
    grid[row][col] = '0'
    for i, j in adjacent(grid, row, col):
        dfs(grid, i, j)
        
    return 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        num_rows, num_cols = len(grid), len(grid[0])
        return sum(dfs(grid, r, c) for r in range(num_rows) 
                                    for c in range(num_cols))



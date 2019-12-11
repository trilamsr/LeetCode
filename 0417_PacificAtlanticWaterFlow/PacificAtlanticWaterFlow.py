def iterator(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            yield i,j

def direction():
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0: continue
            yield i, j
    
def dfs(matrix, aux, row, col, border_row, border_col, visited):
    if col in visited[row]: return aux[row][col]
    if row == border_row or col == border_col: return 1
    if not 0 <= row < len(matrix) or not 0 <= col < len(matrix[0]): return 0
    for i, j in direction():
        y, x = row+i, col+j
        if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]) and matrix[row][col] >= matrix[y][x]:
            explore = dfs(matrix, aux, y, x, border_row, border_col, visited)
            visited[y].add(x)
            if explore: return 1
    return 0
    
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        w = len(matrix[0])
        h = len(matrix)
        visit_pacific = collections.defaultdict(set)
        visit_atlantic = collections.defaultdict(set)
        pacific = [[0]*w for _ in range(h)]
        atlantic = [[0]*w for _ in range(h)]
        for i, j in iterator(matrix):
            pacific[i][j] = dfs(matrix, pacific, i, j, 0, 0, visit_pacific)
            atlantic[i][j] = dfs(matrix, atlantic, i, j, h-1, w-1, visit_atlantic)
        print(pacific)
        print(atlantic)
        return [[i,j] for i,j in iterator(matrix) if pacific[i][j] and atlantic[i][j]]

# ---------------------- FAILED -------------------
def iteration(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            yield i, j

class Solution(object):
    def __init__(self):
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
    def pacificAtlantic(self, matrix):
        if not matrix: return []
        hei = len(matrix)
        wid = len(matrix[0])
        p_visited = [[0 for _ in range(wid)] for _ in range(hei)]
        a_visited = [[0 for _ in range(wid)] for _ in range(hei)]
        for i in range(hei):
            # p_visited[i][0] = True
            # a_visited[i][n-1] = True
            self.dfs(matrix, i, 0, p_visited, hei, wid)
            self.dfs(matrix, i, wid-1, a_visited, hei, wid)
        for j in range(wid):
            # p_visited[0][j] = True
            # a_visited[m-1][j] = True
            self.dfs(matrix, 0, j, p_visited, hei, wid)
            self.dfs(matrix, hei-1, j, a_visited, hei, wid)
        print(p_visited)
        print(a_visited)
        return [[i,j] for i,j in iteration(matrix) if p_visited[i][j] and a_visited[i][j]]
    
    def dfs(self, matrix, i, j, visited, hei, wid):
        visited[i][j] = 1
        for hor, ver in self.directions:
            col, row = i + hor, j + ver
            if col < 0 or col >= hei or row < 0 or row >= wid or visited[col][row] or matrix[col][row] < matrix[i][j]:
                continue
            self.dfs(matrix, col, row, visited, hei, wid)


# ---------------------FAILED-------------------------
def iteration(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            yield i,j
            
def reverse_iteration(matrix):
    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[0])-1, -1, -1):
            yield i, j
            
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        width = len(matrix[0])
        height = len(matrix)
        pacific = [[0]*width for _ in range(height)]
        atlantic = [[0]*width for _ in range(height)]
        # PACIFIC
        for i,j in iteration(matrix):
            if i == 0 or j == 0:
                pacific[i][j] = 1; continue
            top_check = pacific[i-1][j] and matrix[i][j] >= matrix[i-1][j]
            left_check = pacific[i][j-1] and matrix[i][j] >= matrix[i][j-1]
            if top_check or left_check: pacific[i][j] = 1
        # ATLANTIC
        for i,j in reverse_iteration(matrix):
            if i == height-1 or j == width-1:
                atlantic[i][j] = 1; continue
            bottom_check = atlantic[i+1][j] and matrix[i][j] >= matrix[i+1][j]
            right_check = atlantic[i][j+1] and matrix[i][j] >= matrix[i][j+1]
            if bottom_check or right_check: atlantic[i][j] = 1

        return [[i,j] for i,j in iteration(matrix) if pacific[i][j] and atlantic[i][j]]
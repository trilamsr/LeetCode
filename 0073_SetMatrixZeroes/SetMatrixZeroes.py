import itertools

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        firstRowZero = any(matrix[0][x] == 0 for x in range(n))
        firstColZero = any(matrix[y][0] == 0 for y in range(m))
        
        for i, j in self.range_2d(matrix):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
        
        for i, j in self.range_2d(matrix):
            if not i or not j: continue
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        
        if firstRowZero:
            for col in range(n): matrix[0][col] = 0
        if firstColZero:
            for row in range(m): matrix[row][0] = 0
        return matrix
    
    def range_2d(self, mat):
        m, n = len(mat), len(mat[0])
        return itertools.product(range(m), range(n))
        

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = set(), set()
        for i, j in self.range_2d(matrix):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
        for row in row: self.set_row(matrix, row)
        for col in col: self.set_col(matrix, col)
        return matrix

    def set_row(self, mat, row):
        col = len(mat[0])
        for col in range(col):
            mat[row][col] = 0
        
    def set_col(self, mat, col):
        row = len(mat)
        for row in range(row):
            mat[row][col] = 0
    
    def range_2d(self, mat):
        m, n = len(mat), len(mat[0])
        return itertools.product(range(m), range(n))


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n, record = len(matrix), len(matrix[0]), []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0: continue
                record.append((i, j))
        for y, x in record: self.set_zero(matrix, y, x)
        return matrix
    
    def set_zero(self, matrix, i, j):
        directions = [(-1, 0),(0, -1),(1, 0),(0, 1)]
        for di, dj in directions:
            self.set_dir(matrix, i, j, di, dj)
    
    def set_dir(self, mat, i, j, di, dj):
        m, n = len(mat), len(mat[0])
        inbound = lambda y, x: 0 <= y < m and 0 <= x < n
        while inbound(i,j):
            mat[i][j] = 0
            i, j = i+di, j+dj
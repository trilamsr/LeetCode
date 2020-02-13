class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        leng = len(matrix)
        for x in range(0, leng-1):
            for y in range(x, leng-1-x):
                print(f"1: {x},{y}")
                print(f"2: {y}, {leng-1-x}")
                print(f"3: {leng-1-x},{leng-1-y}")
                print(f"4: {leng-1-y}, {x}")
                matrix[x][y], matrix[leng-1-x][leng-1-y] = matrix[leng-1-x][leng-1-y], matrix[x][y]
                matrix[x][y], matrix[leng-1-y][x] = matrix[leng-1-y][x], matrix[x][y]
                matrix[y][leng-1-x], matrix[leng-1-x][leng-1-y] = matrix[leng-1-x][leng-1-y], matrix[y][leng-1-x] 
        print(matrix)


'''
Quadrants:
II | I
----|----
III | IV
'''
def quadrant_ii_coordinates(matrix):
    half_row_count = (len(matrix) + 1) // 2
    half_col_count = len(matrix) // 2
    for row in range(half_row_count):
        for col in range(half_col_count):
            yield row, col
        
def corner_cells(matrix, row, col):
    for _ in range(4):
        row, col = col, len(matrix) - 1 - row
        yield row, col
    
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for row, col in quadrant_ii_coordinates(matrix):
            #'[A,B,C,D] -> [D, A, B, C] (literally rotate right by once)'
            # where A, B, C, D are the 4 corners
            prev = matrix[row][col]
            for i, j in corner_cells(matrix, row, col):
                prev, matrix[i][j] = matrix[i][j], prev

# -------------------------------------
'''
Quadrants:
 II | I
----|----
III | IV
'''
def quadrant_ii_coordinates(matrix):
    half_row_count = (len(matrix) + 1) // 2
    half_col_count = len(matrix) // 2
    for row in range(half_row_count):
        for col in range(half_col_count):
            yield row, col
        
def corner_cells(matrix, row, col):
    for _ in range(3):
        row, col = len(matrix) - 1 - col, row 
        yield row, col
    
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row, col in quadrant_ii_coordinates(matrix):
            for i, j in corner_cells(matrix, row, col):
                matrix[row][col], matrix[i][j] = matrix[i][j], matrix[row][col]
                row, col = i, j
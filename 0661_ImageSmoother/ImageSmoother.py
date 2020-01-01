class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        dp = [[0] * (len(M[0])+1) for _ in range(len(M)+1)]
        for i in range(1,len(M)+1):
            for j in range(1,len(M[0])+1):
                dp[i][j] = M[i-1][j-1] - dp[i-1][j-1] + dp[i][j-1] + dp[i-1][j]
        for r in range(len(M)):
            for c in range(len(M[0])):
                r1, c1 = max(r-1, 0), max(c-1, 0)
                r2, c2 = min(r + 1, len(M)-1), min(c + 1, len(M[0])-1)
                area = ((r2 - r1 + 1) * (c2 - c1 + 1))
                M[r][c] = (dp[r2+1][c2+1] + dp[r1][c1] - dp[r1][c2+1] - dp[r2+1][c1]) // area
        return M


# ----------------------------------------

'''
dp[row][col] gives u all the sum from the origin
up to row, col
however you only want the area of a particular subregion
​
. . . . . .
. . . . . .
. . . . . .
. . . . . .
. . . . D .
. . . . . .
. . . . . .
. . . . . .
​
Dp[d] = 
D D D D D .
D D D D D .
D D D D D .
D D D D D .
D D D D D .
. . . . . .
. . . . . .
. . . . . .
​
lets say we want only an area of a subregion
. . . . . .
. . . . . .
. . A . B .
. . . . . .
. . C . D .
. . . . . .
. . . . . .
. . . . . .
​
Dp[A] = 
​
A A . . . .
A A . . . .
. . . . . .
. . . . . .
. . . . . .
. . . . . .
. . . . . .
. . . . . .
​
Dp[B-1] = 
​
B B B B B .
B B B B B .
. . . . . .
. . . . . .
. . . . . .
. . . . . .
. . . . . .
. . . . . .
​
Dp[C-1] = 
C C . . . .
C C . . . .
C C . . . .
C C . . . .
C C . . . .
. . . . . .
. . . . . .
. . . . . .
​
Dp[D] = 
D D D D D .
D D D D D .
D D D D D .
D D D D D .
D D D D D .
. . . . . .
. . . . . .
. . . . . .
​
. . . . . .
. . . . . .
. . X X X .                OVERLAPS
. . X X X .   = Dp[D] - Dp[C-1] - Dp[B-1] + Dp[A-1]
. . X X X .
. . . . . .
. . . . . .
. . . . . .
​
C/B C/B B B B .
C/B C/B B B B .
C    C  D D D .
C    C  D D D .
C    C  D D D .
.    .  . . . .
.    .  . . . .
.    .  . . . .

LOOK AT WHERE C/B INTERSECTS
because WE DOUBLE COUNTED THE INTERSECTION,
WE NEED TO ADD IT BACK
​
C/B+A C/B+A B B B .
C/B+A C/B+A B B B .
C      C    D D D .
C      C    D D D .
C      C    D D D .
.      .    . . . .
.      .    . . . .
.      .    . . . .
​
​
THIS GIVES US ALL THE SUM OF THOSE IN X
​
'''

def add_values(row, col, image, copy):
    total = 0
    size  = 0
    for d_row in range(-1, 2):
        for d_col in range(-1, 2):
            if 0 <= row+d_row < len(image) and 0 <= col+d_col < len(image[0]):
                total += image[row+d_row][col+d_col]
                size += 1
    copy[row][col] = total//size
                
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        auxiliary = [[0]*len(M[0]) for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                add_values(i, j, M, auxiliary)
        return auxiliary
        


# ---------------------------------------
from copy import deepcopy

def inbound(row, col, image):
    return 0 <= row < len(image) and 0 <= col < len(image[0])

def reflect (row,col, image, copy):
    total = 0
    count = 0
    for d_row in range(-1, 2):
        for d_col in range(-1,2):
            if inbound(row + d_row, col + d_col, image):
                total+=image[row+d_row][col+d_col]
                count+= 1
    copy[row][col] = total//count
            
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        auxiliary = deepcopy(M)
        for i in range(len(M)):
            for j in range(len(M[0])):
                reflect(i,j, M, auxiliary)
        return auxiliary


# M_BRAX SOLUTION

'''
so each point is between [0..255]
255 is an 8 bit number: 11111111

we store the average into original number
by using 8th..15th bit 

average original
00000000 XXXXXXXX

when we look at a particular number for our average,
we only need to look at the first 8 bits

we need to shift everything back to get the
transformation 

'''
class Solution:
    def imageSmoother(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        for row, col in range_2d(mat):
            cell_average = floor_average_cell(mat, row, col)
            mat[row][col] |= cell_average << 8
        for row, col in range_2d(mat):
            mat[row][col] >>= 8
        return mat
    
def range_2d(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            yield row, col                
    
def floor_average_cell(mat, row, col):
    total, size = 0, 0
    for cell in inclusive_surrounding_cells(mat, row, col):
        total += cell & 0xFF
        size += 1
    return total // size

def inclusive_surrounding_cells(mat, row, col):
    for r in range(max(0, row - 1), min(row + 2, len(mat))):
        for c in range(max(0, col - 1), min(col + 2, len(mat[r]))):
            yield mat[r][c]

# -----------------------------

# Halogthenord's Solution

def getCol(array, x, y, width, height):
    if x < 0 or x >= width:
        return []
    result = [] 
    for i in range(y-1, y+2):
        if i >= 0 and i < height:
            result.append( array[i][x]) 
    return result

def average(array, width, height):
    result = []
    for y in range(0, height):
        left = []
        middle = getCol(array, 0, y, width, height)
        right  = getCol(array, 1, y, width, height)
        row = []
        for x in range(1, width+1):
            totLen = len(left) + len(middle) + len(right)
            totSum = sum(left) + sum(middle) + sum(right)
            row.append((int)(totSum / totLen))
            left   = middle
            middle = right
            right  = getCol(array, x+1, y, width, height)
        result.append(row)
    return result


    
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        return average(M, len(M[0]), len(M))
        
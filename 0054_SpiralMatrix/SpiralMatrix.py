'''
if ur going right... u can only go column amount
going down: you can only go down row-1 amount
​
there's edge case when youre going left and up
in the case that you happen to revisit the same place:
aka row_count >= 2 and col>count >= 2
​
​
after we're done with 1 spiral...
there are row-2 rows and col-2 columns left
​
- subtract 2 from row since u remove top and bottom row
- subtract 2 from cols since u remove left and right cols
​
'''
def magnitudes(row_count, col_count):
    yield col_count
    yield row_count - 1
    no_overlap = row_count >= 2 and col_count >= 2
    if no_overlap:
        yield col_count - 1
        yield row_count - 2
        
def spiral_iterator(matrix):
    row_count, col_count = len(matrix), len(matrix[0])
    spiral_count = (min(row_count, col_count) + 1) // 2
    
    directions = itertools.cycle(((0, 1), (1, 0), (0, -1), (-1, 0)))
    row, col = 0, -1
    # pythonic way to not use -drow, dcol
    drow, dcol = next(directions)
    
    for _ in range(spiral_count):
        for vector_magnitude in magnitudes(row_count, col_count):
            for _ in range(vector_magnitude):
                row, col = row + drow, col + dcol
                yield row, col
            drow, dcol = next(directions)
        row_count -= 2
        col_count -= 2
        
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        return [matrix[i][j] for i, j in spiral_iterator(matrix)]



# -----------------------------------------

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        mem, ret = {}, []
        if not matrix: return ret
        row, col = 0, 0
        m, n = len(matrix), len(matrix[0])
        legal = lambda x, y: 0 <= y < m and 0 <= x < n and matrix[y][x] not in mem
        up = False
        while True:
            ret.append(matrix[row][col])
            mem[matrix[row][col]] = True
            if legal(col+1, row) and not up:
                col += 1
            elif legal(col, row+1): row += 1
            elif legal(col-1, row): col -= 1
            elif legal(col, row-1):
                row -= 1
                up = True
                if not legal(col, row-1): up = False
            else: return ret
# -----------------------------------------

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        while matrix:
            edge, *matrix = matrix
            spiral.extend(edge)
            matrix = tuple(zip(*map(reversed, matrix)))
        return spiral



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        matrix = list(reversed(matrix))
        while matrix:
            spiral.extend(matrix.pop())
            matrix = list(zip(*reversed(matrix)))
        return spiral
# -----------------------------------------

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        result = []
        row_count, col_count = len(matrix), len(matrix[0])
        matrix_size = row_count * col_count
        row, col = 0, 0
        drow, dcol = 0, 1
        for _ in range(matrix_size):
            print(matrix)
            result.append(matrix[row][col])
            # mark as visited
            matrix[row][col] = None
            next_row = (row + drow) % row_count
            next_col = (col + dcol) % col_count
            # if we visited something, then change directions
            if not matrix[next_row][next_col]:
                drow, dcol = dcol, -drow
            row += drow
            col += dcol
            print(drow, dcol)
        return result
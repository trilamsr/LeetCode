VISITED = 0

def adjacent(mat, curr):
    for other in range(len(mat)):
        is_friend = mat[curr][other]
        is_not_visited = mat[other][other]
        if is_friend and is_not_visited:
            yield other

def dfs(mat, curr):
    if mat[curr][curr] == VISITED:
        return 0
    
    mat[curr][curr] = VISITED
    for friend in adjacent(mat, curr):
        dfs(mat, friend)

    return 1

class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        return sum(dfs(mat, person) for person in range(len(mat)))






def dfs (M, row):
    is_second_visit = M[row][row] == 0
    if is_second_visit: return 0
    M[row][row] = 0;
    for col in range(len(M)):
        is_friend = M[row][col]
        if is_friend:
            # M[row][col] = 0
            # M[col][row] = 0 
            dfs(M, col)
    return 1

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0;
        return sum(dfs(M, row) for row in range(len(M)))
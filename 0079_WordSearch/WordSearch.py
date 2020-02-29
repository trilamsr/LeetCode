from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        queue = deque(list(word))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.explore(i, j, queue, board): return True
        return False
    
    def explore(self, i, j, queue, board):
        if board[i][j] == '0': return False
        if queue[0] != board[i][j]: return False
        directions = [(0,1), (1, 0), (-1,0), (0, -1)]
        inbound = lambda y, x: 0 <= y < len(board) and 0 <= x < len(board[0])
        cur = queue.popleft()
        board[i][j] = '0'
        if not queue: return True
        for dy,dx in directions:
            if not inbound(i+dy, j+dx): continue
            if self.explore(i+dy, j+dx, queue, board): return True
        queue.appendleft(cur)
        board[i][j] = cur
        return False



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.explore(board, i, j, word, 0, visited):
                    return True
        return False
    
    def inbound(self, y, x, board):
        return 0 <= y < len(board) and 0<= x < len(board[0])
    
    def explore(self, board, i, j, word, start, visited):
        if (i, j) in visited: return False
        if start == len(word)-1 and board[i][j] == word[start]: return True
        if board[i][j] != word[start]: return False
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited.add((i, j))
        for dy, dx in directions:
            d_i, d_j = dy+i, dx+j
            if not self.inbound(d_i, d_j, board): continue
            if self.explore(board, d_i, d_j, word, start+1, visited):
                return True
        visited.remove((i, j))
        return False
            
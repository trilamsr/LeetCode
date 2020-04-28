import collections

def count_coin(maze):
    ret = set()
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2: ret.add((i, j))
    return ret

def neighbor(i, j, maze):
    directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    inbound = lambda y, x: 0 <= y < len(maze) and 0 <= x < len(maze[0])
    for di, dj in directions:
        if not inbound(i+di, j+dj): continue
        yield i + di, j + dj

def bfs(start, maze, conditions):
    level = 0
    visited = set([start])
    stack = collections.deque([start])
    while stack:
        for _ in range(len(stack)):
            i, j = stack.popleft()
            if conditions(i, j): return level, (i, j)
            for neii, neij in neighbor(i, j, maze):
                if (neii, neij) in visited: continue
                if maze[neii][neij] == 1: continue
                visited.add((neii, neij))
                stack.append((neii, neij))
        level += 1
    return -1, start

def minMoves(maze, x, y):
    print(maze, x, y)
    if maze[x][y] == 1 or maze[0][0] == 1: return -1
    coins = count_coin(maze)
    start = (0,0)
    step = 0
    while len(coins) != 0:
        next_steps, end = bfs(start, maze, lambda i, j: (i, j) in coins)
        if next_steps == -1: return -1
        coins.remove(end)
        start, step = end, step+next_steps
    final_step, end = bfs(start, maze, lambda i, j: i == x and j==y)
    if final_step == -1: return -1
    return step + final_step
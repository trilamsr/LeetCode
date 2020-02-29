1. You have a pair of numbers (A, B) on which you can add together to get 
new tuple (A + B, B) or (A, A + B)

2. (A, B) is initialized to (1, 1).
For any N > 0, find the minimum number of operations 
you need to perform on (A, B) until A = N or B = N

                                        1,1
                        2,1                             1,2
            3, 1                 2, 3           3, 2            1, 3

def adjacent(a,b):
    yield (a+b, b)
    yield (a, a+b)

def bfs(n):
    if n == 1: return 0
    queue = collections.deque((1,1))
    visited, ret = set(), 0
    while queue:
        for _ in range(len(queue)):
            a,b = queue.popleft()
            for child_a, child_b in adjacent(a,b):
                if child_a == n or child_b == n: return ret+1
                if nei not in visited:
                    queue.append(nei)
                    visited.add(nei)
        ret += 1

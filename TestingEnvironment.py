import heapq
from itertools import cycle
from collections import deque
from pprint import pprint
import random

def vector_magnitude(row, col):
    yield col
    yield row - 1
    no_overlap = row > 1 and col > 1
    if no_overlap:
        yield col - 1
        yield row - 2

def update(mat, coordinates, val):
    while coordinates:
        i, j = coordinates.popleft()
        mat[i][j] = heapq.heappop(val)

def sortMatrix(mat):
    row, col = len(mat), len(mat[0])
    ring_cnt = (min(row, col)+1)//2
    directions = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    i, j = 0, -1
    values, coordinates = [], deque()

    for _ in range(ring_cnt):
        for mag in vector_magnitude(row, col):
            di, dj = next(directions)
            for _ in range(mag):
                i, j = i+di, j + dj
                coordinates.append((i, j))
                heapq.heappush(values, mat[i][j])
        row, col = row - 2, col - 2
        update(mat, coordinates, values)
    return mat

def main(N):
    mat = [[random.randint(0, 100) for _ in range(N)] for _ in range(N)]
    sortMatrix(mat)
    pprint(mat)

main(10)
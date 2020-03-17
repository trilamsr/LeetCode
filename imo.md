# IMO Interview Questions

# 1: Salary
Sample input :

    Candidates | Skill | Salary
    =========================
    Alice      |   10  |  80k
    Bob        |   3   |  50k
    Chris      |   4   |  40k
    Donna      |   5   |  60k
    Edgar      |   2   |  70k

Constraints:

1. Number of employees ~= 10 000
2. Salary range: 10k - 1mln, rounded to full 1000s
3. Budget: 10k - 50 mln, rounded to full 1000s

We can have different hiring strategies.


## Company A:



Budget oriented - hire best engineers given set budget (total compensation for the team). Maximize skill given budget

    Budget 130k
    Bax skill: 14 (Alice + Chris)
    80k + 40k = 120k  (10k left, there is noone more they can hire for that)

    Donna + Edgar = 130k, 7 skill levels in total; inferior
    Donna + Chris = 100k , 9l

>List<Person> (Person.wage, Person.skill), int Budget



## Company B:

Project oriented - hire cheapest engineers that can fullfill project needs (total skill level)

    skil target 15
    minimum wages: 140k (Alice + Donna)

## Company C:

Headcount oriented - need to hire K people, and pay them fairly (according to their skills)

    For instance, If you hired Edgar and Chris, you need to pay minimum 70k to Edgar. But Chris's skill is 2x the rate of Edgar, so he has to be paid 2x more than Edgar.

    Hire 2 engineers with fair wages
    Minimum wages: 108k (Donna + Chris)




# 2 Best possible path
---------------------------------------------
Given a matrix M x N , inside the matrix we have integers from 1, 2, ... MN uniquely

    4 3 9
    1 2 8
    5 6 7

    Define path: top-left to bottom right, can only move down or right
    1. 4 3 9 8 7
    2. 4 1 2 8 7

    Best-path: lexigraphically
    1. 3 4 7 8 9
    2. 1 2 4 7 8 (better)

Goal: find the best-path given a MxN matrix?

brute-force complexity?

m = row
n = col
paths = m+nCm

comparation
k =  paths * m+n log (m+n)

1. 3 4 7 8 9
2. 1 2 4 7 8
3. 3 5 6 7 8

O(paths*(m+n)) + paths * (m+n) log(m+n))




def find_max_path(grid):
    address = address_book(grid)
    start = 0, 0
    end = m-1, n-1
    ret = []
    recurse(start, end, address, ret, grid)
    return ret

def address(grid):
    ret = {}
    for i in range(m):
        for j in range(n):
            ret[grid[i][j]] = (i, j)
    return ret
    
def recurse(start, end, address, ret, grid):
    if start == end:
        ret.append(grid[start.i][start.j])
        return
    min = find_min(start, end, grid, address)
    recurse(start, min, address, ret, grid)
    recurse(min, end, address, ret, grid)
    
def find_min(start, end, grid, address):
    ret = math.inf
    for i in range(start.i):
        for j in range(i, end.j):
            ret = min(grid[i][j])
    return address[ret]
            


# 3 Rectangles
==========


    ^    +------------------+-------------------------------------------+
    |    |                  ^                                           |
    |    |                  | y_i                                       |
    |    |                  v                                           |
    |    |         +--------+-----+----+                                |
    |    |         |              ^    |                                |
    |    |   x_i   |              |    |                                |
    |    +<------->+              |h_i |    +-------------------+       |
    |    |         |     w_i      |    |    |                   |       |
    |    |         +<----------------->+    |                   |       |
    |    |         |              v    |    |                   |       |
    |H   |         +--------------+----+----|----+              |       |
    |    |                        |         |    |              |       |
    |    |                        |         |    |              |       |
    |    |   +--------------------+         |    |              |       |
    |    |   |                    |---------|-----              |       |   ...
    |    |   |                    |         |                   |       |   ... new window
    |    |   |              +---------------------+             |       |   ...
    |    |   |              |#####|.........|#####|             |       |
    |    |   |              |#####|.........+-------------------+       |   ###
    |    |   +--------------------+...............|                     |   ### overlap
    |    |                  |.....................|                     |   ###
    v    +------------------+---------------------+---------------------+
                                                                    (W,H)
        <-------------------------------------------------------------->
                                        W




Input:
  W, H <= 10,000 width and height of browser.
  n <= 30 existing windows, given by tuples (x_i, y_i, w_i, h_i). These will be non-overlapping.
  new_w, new_h: width and height of new window.

Ouput:
  new_x, new_y: the top left corner, where to position the new window, minimizing the total overlap area with existing windows.
  if there are many positions with the same total overlap, return any of them.
  

There will always be a solution, for which the final rectangle touches one existing rectangle from the left or from the right AND one existing rectangle from the top or from the bottom.

n*n*n


def find_coordinate(windows, w, h, window_w, window_h):
    ret = -1, -1
    overlap = math.inf
    for window1 in windows:
        for window2 in windows:
            for start_i, start_j in coordinates(window1, window2):
            cur_overlap = overlap(window_w, window_h, start_i, start_j, windows)
            if cur_overlap < overlap:
                overlap = cur_overlap
                ret = i, j
    return ret
    
def coordinates(window1, window2):
    # left of window1, top of window2
    new_x = window1.x - new_w  # left of w1
    new_y = window2.y - new_h  # top of w2
    coordinates.append((new_x, new_y))
    
    # left of window1, bottom of window2
    # right of window1, top of window2
    # right of window1, bottom of window2

def overlap_two_windows(window1, window2):
   window1 = (x_1, y_1, w_1, h_1)
   window2 = (x_2, y_2, w_2, h_2)
   row_overlap = x_1 < x_2 <= x_1+w_1 or  x_2 < x_1 <= x_2 + w_2 
   col_overlap = y_1 < y_2 <= y_2+h_2 or  y_2 < y_1 <= x_y2 + w_2
   if row_overlap and col_overlap:
        wid = abs(max(x_1, x_2) - min(x_1+w_1, x_2+w_2))
        hei = abs(max(y_1, y_2) - min(y_1+h_1, y_2+h_2))
        return wid*hei
    return 0


    +------------------+
    |                  |           
    |                  |       
    |                  |           
    |         +--------+-----+----+
    |         |########|          |
    |         |########|          |
    +<------->+--------|          |
              |                   |    
              +                   +
              |                   |
              +--------------+----+





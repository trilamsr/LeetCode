# 4. Bob Navigates a Maze

Bob and Alice have teamed up on a game show. After winning the first round, they now have access to a maze with hidden gold. If Bob can collect all the gold coins and deliver them to Alice's position, they can split the gold.

Bob can move horizontally or vertically as long as he stays in the maze, and the cell is not blocked.The maze is represented by an n × m array.
Each cell has a value, where 0 is open, 1 is blocked, and 2 is open with a gold coin. 

Bob starts at the top left in cell in (row, column) = (0, 0). Alice's position is given by (x,y).

Determine the shortest path Bob can follow to collect all gold coins and deliver them to Alice. If Bob can't collect and give all the gold coins, return -1.

**Example:**

    Input:
        maze = [[0,2,1],[1,2,0],[1,0,0]] with Alice at (2,2) is represented as follows:
        B represents Bob’s starting position at (0,0), and A represents Alice’s position (which will also be Bob’s final position).
        As Bob starts at (0,0), he has two possible paths to collect the gold and deliver to Alice: (0, 0) → (0, 1) → (1, 1) → (2, 1) → (2, 2) and (0, 0) → (0, 1) → (1, 1) → (1, 2) → (2,2). Both paths have a length of 4 and could represent the shortest path.
        
        
**Function Description**
    
    The function must return the integer length of Bob's shortest path, or -1 if it's not possible.
    minMoves has the following parameter(s):
        maze[maze[0][0],...maze[n-1][m-1]]: a 2D array of integers
        x: an integer denoting Alice's row coordinate
        y: an integer denoting Alice's column coordinate
        Constraints: ≤ n, m ≤ 1000 ≤ the number of coins ≤ 101 ≤ x < n1 ≤ y < m
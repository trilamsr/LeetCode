# 7. Number of Moves

Given a chess board of n rows (top to bottom) and n columns (left to right).
In each move, a knight moves either: 2 column positions and 1 row position2 row positions and 1 column position. In other words, a move is 2 steps along one axis and 1 step along a perpendicular axis.

Given a starting position A and ending position B, calculate the minimum number of moves needed by the knight to move from A to B if it is possible. If it is not possible, return -1.

**Example:** 

    Inputs:
        n = 9
        startRow = 4
        startCol = 4
        endRow = 4
        endCol = 8

    Ouput: 2
        Explanation: The chess board has a size of 9 x 9.Starts at the position (startRow, startCol) = (4, 4).
        Move 1 step up or down, then 2 steps right to reach either the position (3, 6) or (5,6). Move 2 steps right and 1 step down or up as necessary to reach the position (4,8).
        The minimum number of moves to move from the position (4, 4) to the position (4, 8) is 2.

## Function Description:
    
- minMoves has the following parameters:
- int n: the width and height of the square board
- int startRow: the row of the starting location
- int startCol: the column of the starting location
- int endRow: the row of the target location
- int endCol: the column of the target location
- Returns: int: a single integer that denotes the number of moves required or -1 if it is not possible to reach the target location.
        
>Constraints: 4 ≤ n ≤ 1500 ≤ startRow, startCol, endRow, endCol < n
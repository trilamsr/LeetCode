class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ret = []
        queen_locations = {(x,y) for x,y in queens}
        for coordinate in self.locations(king, queen_locations):
            ret.append(coordinate)
        return ret
    
    def locations(self, king, queens_locations):
        row, col = king
        for d_row in range(-1, 2):
            for d_col in range(-1, 2):
                if d_row == d_col == 0: continue
                cur_row, cur_col = row, col
                found = False
                while self.valid(cur_row, cur_col, found):
                    cur_row += d_row
                    cur_col += d_col
                    if (cur_row, cur_col) in queens_locations:
                        yield cur_row, cur_col
                        found = True

    def valid(self, row, col, status):
        return 0 <= row < 8 and 0 <= col < 8 and not status
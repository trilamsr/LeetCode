
# O(n) Time and O(n) in Space

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 2 or numRows < 2: return s
        mem = [[] for _ in range(numRows)]
        for i, row in self.iterator(s, numRows):
            mem[row].append(s[i])
        return ''.join([''.join(row) for row in mem])
    
    def iterator(self, s, numRows):
        cur_row, cur_i, is_down = 0, 0, 1
        while cur_i < len(s):
            for i in range(numRows-1):
                if cur_i >= len(s): return
                yield cur_i, cur_row
                cur_i, cur_row = cur_i+1, cur_row+is_down
            is_down = -1 if is_down == 1 else 1

# O(n) Time and O(n*k) in Space / SPARSE/This solution come from the code below
class Solution:
    def iterator(self, s, numRows):
        i, j, count = 0, 0, 0
        direction = itertools.cycle(((1, 0), (-1, 1)))
        while count < len(s):
            d_i, d_j = next(direction)
            for _ in range(numRows-1):
                if count >= len(s): return
                yield i, j, count
                i, j, count = i+d_i, j+d_j, count+1
            
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 2 or numRows < 2: return s
        mem = [[""]*len(s) for _ in range(numRows)]
        for i, j, count in self.iterator(s, numRows):
            mem[i][j] = s[count]
        return ''.join([''.join(row) for row in mem])


# Halogthenord
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = []
        for i in range(0,numRows):
            row.append([])
        length = len(s)
        stringIndex = 0
        rowIndex = 0
        result = ""
        while stringIndex < length:
            if rowIndex == 0:
                for i in range(0,numRows):
                    row[i].append(s[stringIndex])
                    stringIndex += 1
                    if stringIndex >= length: break
                rowIndex = numRows - 2
                rowIndex = 0 if rowIndex < 0 else rowIndex
            else:
                row[rowIndex].append(s[stringIndex])            
                stringIndex += 1
                rowIndex -= 1
        for r in row:
            result += ''.join(r)
        return result


# m_brax
def row_iterator(word, row_count):
    row = 0
    delta_row = 1
    for ch in word:
        yield row, ch
        next_location = row + delta_row
        out_of_bounds = next_location < 0 or next_location == row_count
        if out_of_bounds:
            delta_row *= -1
        row += delta_row

class Solution:
    def convert(self, word: str, row_count: int) -> str:
        if len(word) == 0 or row_count == 0:
            return ""
        row_buffer = [[] for _ in range(row_count)]
        for row, char in row_iterator(word, row_count):
            row_buffer[row].append(char)
        result_buffer = []
        for row in row_buffer:
            result_buffer.extend(row)
        return "".join(result_buffer)















class Solution:
    def myAtoi(self, str: str) -> int:
        ret, is_positive = [], 1
        first_alpha, first_num = -1, -1 
        for i, v in enumerate(str):
            if v.isdigit() or v in '+-':
                ret.append(v)
                if first_num < 0: first_num = i
            if v.isalpha() and first_alpha < 0:
                first_alpha = i
        
        if first_alpha > first_num: return 0
        ret = int(''.join(ret))
        if -(1<<31) > ret: return -(1<<31)
        if ret > (2**31)-1: return (2**31)-1
        return ret*is_positive
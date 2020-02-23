from math import inf
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3: return False
        for i in range(n-1):
            first = self.parse_val(num, 0, i)
            if first == inf: continue
            for j in range(i+1, n-1):
                second = self.parse_val(num, i+1, j)
                if second == inf: continue
                if self.dfs(num, first, second, j+1): return True
        return False
    
    def parse_val(self, num, start, end):
        if num[start] == "0" and start != end:
            return inf
        return int(num[start:end+1])
    
    def dfs(self, num, first, second, start):
        if start >= len(num): return True
        total = first+second
        for val, end in self.adjacent(num, start):
            if val == total and self.dfs(num, second, first+second, end):
                return True
        return False
    
    def adjacent(self, num, start):
        for end in range(start, len(num)):
            val = self.parse_val(num, start, end)
            yield val, end+1
    

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if not num: return True
        if len(num) < 3: return False
        for i in range(1, n):
            for j in range(i+1, n):
                a, b, c = num[:i], num[i:j], num[j:]
                total = str(int(a) + int(b))
                while c.startswith(total):
                    a, b, c = b, c[:len(total)], c[len(total):]        
                    total = str(int(a) + int(b))
                    if not c: return True
        return False

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        cap = len(num)//2+1
        for a_len in range(1, cap):
            if num[0] == '0' and a_len > 1: return False
            for b_len in range(1, cap):
                if num[a_len] == '0' and b_len > 1: continue
                c_start = a_len+b_len
                a, b, c = num[:a_len], num[a_len:c_start], num[c_start:]
                if self.explore_case(a,b,c): return True
        return False
    
    def explore_case(self, a,b,c):
        total = str(int(a) + int(b))
        while c.startswith(total):
            a, b, c = b, c[:len(total)], c[len(total):]
            total = str(int(a) + int(b))
            if not c: return True
        return False



# NEL_TU_
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        N = len(num)
        if N < 3: return False
        for i in range(1, N-1):
            for j in range(i+1, N):
                a, b = num[:i], num[i:j]
                if i > 1 and num[0] == '0' or j-i > 1 and num[i] == '0': continue
                a, b = int(a), int(b)
                c = a + b
                while num[j:].startswith(str(c)):
                    j += len(str(c))
                    a, b, c = b, c, b+c
                if j >= N:
                    return True
        return False
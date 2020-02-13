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
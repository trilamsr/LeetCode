class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        self.dfs(1, n+1, k, ret, [])
        return ret
    
    def dfs(self, start, end, leng, ret, stack):
        if leng == 0:
            ret.append(stack[:])
            return
        for i in range(start, end):
            stack.append(i)
            self.dfs(i+1, end, leng-1, ret, stack)
            stack.pop()

class Solution:
    def has_k_bits(self, num, k):
        count = 0
        while num:
            count += 1
            num &= num-1 
        return count == k
    
    def get_digits(self, num, upper_bound):
        ret = []
        for i in range(upper_bound):
            if (num & (1<<i)) > 0: ret.append(i+1)
        return ret
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        for i in range(1<<n):
            if self.has_k_bits(i, k):
                ret.append(self.get_digits(i, n))
        return ret
    
    
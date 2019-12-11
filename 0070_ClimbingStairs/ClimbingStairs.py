class Solution:
    def __init__(self):
        self.mem = {}
        self.mem[1] = 1
        self.mem[2] = 2
        
    def climbStairs(self, n: int) -> int:
        if not n: return 0
        if n in self.mem: return self.mem[n]
        self.mem[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.mem[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 0, 1
        for i in range(n):
            x, y = y, x+y
        return y
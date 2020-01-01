class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            ret += 1
            n &= (n-1)
        return ret

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(((n>>i) & 1) for i in range(32))

class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        for i in range(32):
            ret += ((n>>i) & 1)
        return ret
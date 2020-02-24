class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = self.parse_int(num1)
        b = self.parse_int(num2)
        return str(a+b)
    
    def parse_int(self, num):
        if num[0] == '0': return 0
        ret = 0
        for digit in num:
            cur = 1*int(digit)
            ret = ret*10+cur
        return ret
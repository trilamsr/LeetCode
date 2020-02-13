class Solution:
    @staticmethod
    def first_valid_index(s):
        if not s: return -1
        i = 0
        while s[i] == " ":
            i += 1
            if i == len(s):return -1
        return i
    
    @staticmethod
    def get_digits(s, i):
        while i < len(s) and s[i].isdigit():
            yield int(s[i])
            i += 1
    
    @staticmethod
    def clamp_32(num):
        INT_MAX = (2**31)-1
        INT_MIN = -(1<<31)
        num = max(num, INT_MIN)
        num = min(num, INT_MAX)
        return num
        
    def myAtoi(self, str: str) -> int:
        i = Solution.first_valid_index(str)
        if i == -1: return 0
        sign = -1 if str[i] == '-' else 1
        digit_start = i+1 if str[i] in '+-' else i
        ret = 0
        for num in Solution.get_digits(str, digit_start):
            ret = (ret*10)+num
        return Solution.clamp_32(ret*sign)
        
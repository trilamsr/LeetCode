def is_overflowed(x):
    return x >= 2**31-1 or x <= -2**31
    
class Solution:
    def reverse(self, x: int) -> int:
        if is_overflowed(x): return 0
        s = str(x)[::-1]
        ret = int(s) if s[-1] != '-' else -1*int(s[:-1])
        return ret if not is_overflowed(ret) else 0
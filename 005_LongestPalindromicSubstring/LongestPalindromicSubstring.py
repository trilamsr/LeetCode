# Top-down recursive-----------------------------
class Solution:
    def __init__(self):
        # dp[i][j] = 1 for True, 2 for False, 0 for unvisited
        # without this it can't differentiate between false and unvisited, so end up doing repeated work and time out at longer string 
        self.dp = []
    
    def top_down_palindrome(self, i, j, s):
        if i >= j: return 1
        if s[i] != s[j]: return 2
        if self.dp[i][j]: return self.dp[i][j]
        self.dp[i][j] = self.top_down_palindrome(i+1, j-1, s)
        return self.dp[i][j]
        
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.dp = [[0]*n for _ in range(n)]
        if n < 2: return s
        for sub_str_len in range(n, -1, -1):
            for beg in range(n-sub_str_len):
                if self.top_down_palindrome(beg, beg+sub_str_len, s) == 1:
                    return s[beg:beg+sub_str_len+1]
        


# Bottom-up iterative-------------------------------------

# Using array
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if len(s) <= 1: return s
        dp = [[0]*n for _ in range(n)]
        lo, hi = 0, 0
        for leng in range(n):
            for start in range(n-leng):
                end = start + leng
                if s[start] != s[end]: continue
                dp[start][end] = leng <= 1 or dp[start+1][end-1]
                if dp[start][end] and end-start > hi-lo:
                    lo, hi = start, end
        return s[lo:hi+1]

# Using dictionary instead of array
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if len(s) <= 1: return s
        mem = {}
        lo, hi = 0, 0
        for leng in range(n):
            for start in range(n-leng):
                end = start + leng
                if s[start] != s[end]:
                    mem[start, end] = 0
                    continue
                mem[start, end] = leng <= 1 or mem[start+1, end-1]
                if mem[start, end] and end-start > hi-lo:
                    lo, hi = start, end
        return s[lo:hi+1]


# Better expand from center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lo, hi = 0, 0
        if len(s) < 2: return s
        for i in range(len(s)):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i+1)
            lo, hi = max((odd, even, (lo, hi)), key = lambda x: x[1]-x[0])
        return s[lo:hi+1]
    
    def expand(self, s, lo, hi):
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo, hi = lo-1, hi+1
        return lo+1, hi-1

# expand from center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lo, hi = 0, 0
        if len(s) < 2: return s
        for i in range(len(s)):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i+1)
            leng = max(odd, even)
            if leng > hi-lo:
                lo, hi = i - (leng-1)//2, i + (leng//2)
        return s[lo:hi+1]
    
    def expand(self, s, lo, hi):
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo, hi = lo-1, hi+1
        return hi - lo - 1



# 1st success
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n): 
            dp[i][i] = 1
            if i == 0: continue
            if s[i] == s[i-1]: dp[i][i-1] = 1
        start, end = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                left, right = j-1-i, j
                if s[left] == s[right]: dp[left][right] = dp[left+1][right-1]
                if dp[left][right] and right-left > end-start: start, end = left, right
        return s[start:end+1]



# @M-brax-----------------------------------------------------------------------------
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        cache = {}

        def check_palindrome(start, end):
            if end <= start:
                return True
            elif s[start] != s[end]:
                return False
            elif (start, end) in cache:
                return cache[start, end]
            else:
                cache[start, end] = check_palindrome(start + 1, end - 1)
                return cache[start, end]
        
        size = len(s)
        for substrlen in range(size-1, -1, -1):
            for start in range(size - substrlen):
                end = start + substrlen
                is_palindrome = check_palindrome(start, end)
                if is_palindrome:
                    return s[start:end+1]
        return ''


from collections import namedtuple
Palindrome = namedtuple("Palindrome", "lo hi")
def expand(s, lo, hi):
    while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
        lo -= 1
        hi += 1
    return Palindrome(lo + 1, hi - 1)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        ret = Palindrome(lo=0, hi=0)
        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i + 1)
            ret = max((odd, even, ret), key=lambda p: p.hi - p.lo)
        return s[ret.lo : ret.hi + 1]

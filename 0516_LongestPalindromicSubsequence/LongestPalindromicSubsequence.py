class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        return self.recurse(s, dp, 0, len(s)-1)
    
    def recurse(self, s, dp, left, right):
        if (left, right) in dp: return dp[(left, right)] 
        if left > right: return 0
        if left == right: return 1
        if s[left] != s[right]:
            shrink_left = self.recurse(s, dp,left+1, right)
            shrink_right = self.recurse(s, dp, left, right-1)
            dp[(left, right)] = max(shrink_left, shrink_right)
        else:
            dp[(left, right)] = 2 + self.recurse(s, dp, left+1, right-1)
        return dp[(left, right)]
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        short, long = 0, 0
        while long < len(t):
            if t[long] == s[short]: short += 1
            if short >= len(s): return True
            long += 1
        return False


# StefanPochmann's solution

class Solution:
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(char in t for char in s)
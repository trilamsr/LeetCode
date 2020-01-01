class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        lo, hi = 0, len(s)-1
        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1; hi -= 1
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        mem = string.ascii_letters+string.digits
        lo, hi = 0, len(s)-1
        while lo < hi:
            while lo < len(s) and s[lo] not in mem:
                lo += 1
            while hi > 0 and s[hi] not in mem:
                hi -= 1
            if lo > hi or s[lo].lower() == s[hi].lower(): 
                lo += 1
                hi -= 1
            else:
                return False
        return True


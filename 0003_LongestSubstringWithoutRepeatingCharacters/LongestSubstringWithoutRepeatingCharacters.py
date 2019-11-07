class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        left, right = 0,0
        mem = set()
        while left < len(s) and right < len(s):
            if s[right] not in mem:
                mem.add(s[right])
                right+=1
            else: 
                mem.remove(s[left])
                left+=1
            ret = max(ret, len(mem))
        return ret
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        items, ret = set(nums), 0
        while items:
            cur = items.pop()
            left = self.explore(items, cur, -1)
            right = self.explore(items, cur, 1)
            ret = max(ret, 1+left+right)
        return ret
    
    def explore(self, items, cur, delta):
        ret = delta
        while cur+ret in items:
            items.remove(cur+ret)
            ret = ret+delta
        return abs(ret)-1
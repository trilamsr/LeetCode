class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        if not intervals: return ret
        intervals.sort(key = lambda x: x[0])
        beg, end = intervals[0][0], intervals[0][1]
        
        for lo, hi in intervals:
            if lo <= end:
                beg, end = min(lo, beg), max(hi, end)
            else:
                ret.append([beg, end])
                beg, end = lo, hi
        ret.append([beg, end])
        return ret
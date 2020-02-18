# The Idea is to sort the interval by the ending number
# Starting with the base case (first interval of the sorted once).
# For other intervals, we check if their starting is less than the cur, end.
# If it is, ignore it, or ret += 1
# If it's not, then it's valid. cur_end = new end



class Solution:
    # Build-in sort
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda intervals: intervals[1])
        cur_beg = cur_end = None
        ret = 0
        for beg, end in intervals:
            if not cur_beg: cur_beg, cur_end = beg, end
            else:
                if beg < cur_end:
                    ret += 1
                else:
                    cur_end = end
        return ret


class Solution:
    def merge_sort(self, intervals):
        if len(intervals) < 2: return intervals
        left = self.merge_sort(intervals[:len(intervals)//2])
        right = self.merge_sort(intervals[len(intervals)//2:])
        return self.merge(left,right)
    
    def merge(self, left, right):
        ret, le_ind, ri_ind = [], 0, 0
        while le_ind < len(left) and ri_ind < len(right):
            if left[le_ind][1] < right[ri_ind][1]:
                ret.append(left[le_ind])
                le_ind += 1
            else:
                ret.append(right[ri_ind])
                ri_ind += 1
        if le_ind == len(left):
            ret.extend(right[ri_ind:])
        else:
            ret.extend(left[le_ind:])
        return ret
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = self.merge_sort(intervals)
        cur_beg = cur_end = None
        ret = 0
        for beg, end in intervals:
            if not cur_beg: cur_beg, cur_end = beg, end
            else:
                if beg < cur_end:
                    ret += 1
                else:
                    cur_end = end
        return ret
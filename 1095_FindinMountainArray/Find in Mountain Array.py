# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        peak = self.PeakIndex(0, size-1, mountain_arr)
        leftSearch = self.find(0, peak, mountain_arr, target, True)
        return leftSearch if leftSearch != -1 else self.find(peak+1, size-1, mountain_arr, target, False)
    
    def peakIndex(self, lo, hi, arr):
        while lo <= hi:
            mid = (lo+hi)//2
            if arr.get(mid+1) - arr.get(mid) < 0:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
    
    def find(self, lo, hi, arr, target, is_left):
        while lo <= hi:
            mid = (lo+hi)//2
            midVal = arr.get(mid)
            if midVal == target:
                return mid
            if is_left == (midVal > target):
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

# ------------------------------------------------------------
def lower_bound(lo, hi, property):
    while lo <= hi:
        mid = (lo + hi) // 2
        if property(mid):
            hi = mid - 1
        else:
            lo = mid + 1
    return lo

class Solution:
    def findInMountainArray(self, target: int, mtn: 'MountainArray') -> int:
        mono_decreasing = lambda x: mtn.get(x) > mtn.get(x+1)
        leq_target = lambda x: mtn.get(x) <= target
        gte_target = lambda x: mtn.get(x) >= target
        
        n = mtn.length()
        peak_idx = lower_bound(0, n-1, mono_decreasing)
        
        ret = lower_bound(0, peak_idx, gte_target)
        if mtn.get(ret) != target:
            ret = lower_bound(peak_idx + 1, n-1, leq_target)
    
        return ret if (ret < n and mtn.get(ret) == target) else -1
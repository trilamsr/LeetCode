class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lo, hi = 0, len(A)-1
        while lo <= hi:
            mid = (hi+lo)//2
            if A[mid] > A[mid+1]:
                hi = mid-1
            else:
                lo = mid+1
        return lo
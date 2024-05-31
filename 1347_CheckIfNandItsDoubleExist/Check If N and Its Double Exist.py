from collections import Counter
from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        memo = Counter(arr)
        if 0 in memo and memo[0] > 1: return True
        for n in memo:
            if n == 0: continue
            if n*2 in memo: return True
        return False

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i, val in enumerate(arr):
            l, r = 0, len(arr)
            target_ind = self.contain_target(arr, val*2,l, r)
            if target_ind == -1 or target_ind == i: continue
            return True
        return False

    def contain_target(self, arr, target, l, r):
        while l < r:
            mid = (l+r)//2
            print(l, r, arr[mid])
            if arr[mid] == target: return mid
            if arr[mid] < target:
                l = mid+1
            else:
                r = mid
        return -1
        


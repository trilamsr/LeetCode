class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            pivot = self.get_pivot(nums, lo, hi)
            lower, upper = self.partitions(nums, lo, hi, pivot)
            if lower <= k <= upper: break
            if k < lower: hi = lower-1
            if k > upper: lo = upper+1
        return nums[k-1]
    
    def get_pivot(self, nums, lo, hi):
        mid = (lo+hi)//2
        ret = sorted([nums[x] for x in (lo, hi, mid)])
        return ret[1]
        
    def swap(self,arr, a,b):
        arr[a], arr[b] = arr[b], arr[a]
    
    def partitions(self, nums, lo, hi, pivot):
        ind = lo
        while ind <= hi:
            if nums[ind] > pivot:
                self.swap(nums, lo, ind)
                ind += 1
                lo += 1
            elif nums[ind] < pivot:
                self.swap(nums, hi, ind)
                hi -= 1
            else:
                ind += 1
        return lo, hi
                

import heapq

class Heap:
    def __init__(self, k):
        self.capacity = k
        self.heap = []
        
    def add(self, element):
        if len(self.heap) < self.capacity:
            heapq.heappush(self.heap, element)
        else:
            heapq.heappushpop(self.heap, element)
    
    def k_largest(self):
        return self.heap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap(k)
        for num in nums:
            heap.add(num)
        return heap.k_largest()
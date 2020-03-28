from heapq import heappush, heappop
from itertools import islice

class Node:
    def __init__(self, A, B, i, j):
        self.i = i
        self.j = j
        self.total = A[i] + B[j]
    
    def __lt__(self, other):
        return self.total < other.total

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or not k: return []
        it = self.sorted_pairs(nums1, nums2)
        return self.take(it, k)
        
    def take (self, iterable, n):
        return list(islice(iterable, n))
    
    def sorted_pairs(self, A, B):
        origin = Node(A, B, 0, 0)
        heap = [origin]
        visited = set(((0,0)))
        while heap:
            node = heappop(heap)
            yield [A[node.i],B[node.j]]
            for nei in self.neighbor(node, A, B):
                if (nei.i, nei.j) in visited: continue
                heappush(heap, nei)
                visited.add((nei.i, nei.j))
                
    def neighbor(self, node, A, B):
        for nei_i, nei_j in self.dirs(node.i, node.j):
            if 0 <= nei_i < len(A) and 0 <= nei_j < len(B):
                yield Node(A, B, nei_i, nei_j)
                
    def dirs(self, i, j):
        yield i+1, j
        yield i, j+1

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or not k: return []
        ret = []
        for a, b, c in self.generate_pairs(nums1, nums2):
            ret.append((b, c))
            if len(ret) == k: break
        return ret
    
    def generate_pairs(self, nums1, nums2):
        heap = []
        for a, b in itertools.product(nums1, nums2):
            heapq.heappush(heap, (a+b, a, b))
        while heap:
            yield heapq.heappop(heap)


import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = collections.Counter(nums)
        heap = heapq.nlargest(k, frequency.items(), key= lambda x: x[1])
        return [x for x, y in heap]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = collections.Counter(nums)
        bucket = self.make_bucket(frequency)
        return self.get_k(bucket, k)
    
    def make_bucket(self, frequency):
        ret = collections.defaultdict(list)
        for k, v in frequency.items():
            ret[v].append(k)
        return ret
    
    def get_k(self, bucket, k):
        ret = []
        start = max(bucket)
        while start and len(ret) < k:
            while bucket[start] and len(ret) < k:
                ret.append(bucket[start].pop())
            start -= 1
        return ret
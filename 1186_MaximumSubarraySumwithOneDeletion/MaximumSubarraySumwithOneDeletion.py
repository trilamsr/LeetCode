class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        it = iter(arr)
        ret = skip = take = next(it)
        for val in it:
            skip = max(take, skip + val) 
            take = max(take + val, val)
            ret = max(skip, take, ret)
        return ret

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        skip = take = arr[0]
        ret = arr[0]
        for i, val in enumerate(arr):
            if i == 0: continue
            skip = max(take, skip + val) 
            take = max(take + val, val)
            ret = max(skip, take, ret)
        return ret

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        take, skip = [arr[0]], [arr[0]]
        for i, val in enumerate(arr):
            if i == 0: continue
            new_skip = max(take[-1], skip[-1]+val)
            skip.append(new_skip)
            new_take = max(take[-1]+val, val)
            take.append(new_take)
        return max(take+skip)
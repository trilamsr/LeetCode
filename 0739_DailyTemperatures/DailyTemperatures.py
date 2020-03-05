class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = [0]*len(T)
        stack = []
        for i in range(len(T)-1, -1, -1):
            cur_temp = T[i]
            while stack and cur_temp >= T[stack[-1]]:
                stack.pop()
            ret[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return ret

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = [0]*len(T)
        record = {}
        for i in range(len(T)-1, -1, -1):
            ret[i] = self.check_record(i, T[i], record)
            record[T[i]] = i
        return ret
    
    def check_record(self, ind, cur_temp, record):
        ret = math.inf
        for temp in range(cur_temp+1, 101):
            if temp in record:
                ret = min(ret, record[temp])
        return ret - ind if ret != math.inf else 0
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ret = []
        for hr in range(12):
            for minute in range(60):
                config = (hr<<6)|minute
                if self.count_one(config, num):
                    ret.append(f"{hr}:{minute:02}")
        return ret
    
    def count_one(self, config, k):
        count = 0
        while config:
            config &= config-1
            count+=1 
        return k == count

# ----------------------------------------

class Solution:
    def __init__(self):
        self.time = [1,2,4,8,16,32,1,2,4,8]
        
    def readBinaryWatch(self, num: int) -> List[str]:
        ret = []
        for config in range(1<<10):
            if self.count_one(config, num):
                is_valid, hr, minute = self.valid_time(config)
                if is_valid: ret.append(f"{hr}:{minute:02}")
        return ret
    
    def count_one(self, config, k):
        count = 0
        while config:
            config &= config-1
            count+=1 
        return k == count
    
    def valid_time(self, config):
        hr, minute = 0, 0
        for i in range(10):
            if config & 1<<i:
                if i >= 6: hr += self.time[i]
                else: minute += self.time[i]
        return hr < 12 and minute < 60, hr, minute
        

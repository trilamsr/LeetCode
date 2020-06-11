from itertools import groupby
class Solution:
    def process(self, start):
        buffer = []
        for digit, group in itertools.groupby(start):
            count = str(len(list(group))) # eg. the 2 in two 1s 
            buffer.append(count+digit) # create the 21 string and accumulate it
        return ''.join(buffer)
    
    def countAndSay(self, n: int) -> str:
        start = '1'
        for _ in range(n-1):
            start = self.process(start)
        return start
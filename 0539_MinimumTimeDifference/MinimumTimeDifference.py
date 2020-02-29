class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        allTime = [self.get_absolute(time) for time in timePoints]
        distance = self.get_min(allTime)
        return distance
    
    def get_min(self, arr):
        dis = math.inf
        for a, b in self.pairs(arr):
            dis = min(dis, abs(b-a), (1440-a+b))
        return dis
    
    def get_absolute(self, time):
        h, m = time.split(':')
        return (int(h)*60+int(m))%1440
    
    def pairs(self, arr):
        arr.sort()
        for i in range(0, len(arr)):
            yield arr[i-1], arr[i]
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ret = [0]*(n+1)
        while bookings:
            start, end, count = bookings.pop()
            ret[start-1] += count
            ret[end] -= count
        self.prefix_sum(ret)
        return ret[:n]
    
    def prefix_sum(self, arr):
        for i in range(1, len(arr)):
            arr[i] = arr[i] + arr[i-1]